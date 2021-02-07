from wsgiref import simple_server
import falcon
import json
import base64
import yaml
import sys
import copy

try:
    with open('init_state.yaml') as file:
        init_state = yaml.safe_load(file)
    with open('expect_state.yaml') as file:
        expect_state = yaml.safe_load(file)
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

registered = {
    'user': init_state['access'][0]['username'],
    'pswd': init_state['access'][0]['password'],
    'contract_id': init_state['access'][0]['contract_id'],
}

issued_token = []
auth_header_type = 'Bearer'


class AccessTokenException(Exception):
    pass


def auth(req, resp):
    try:
        at = req.headers['AUTHORIZATION'][len(auth_header_type)+1]
        if at in issued_token:
            raise AccessTokenException
    except IndexError:
        resp.status = falcon.HTTP_400
        resp.body = json.dumps({
            'message': 'no access token'
        })
        return False
    except AccessTokenException:
        resp.status = falcon.HTTP_401
        resp.body = json.dumps({
            'message': 'invalid access token'
        })
        return False
    return True


class AccessResource:
    def on_post(self, req, resp, contract_id):
        usps = base64.b64decode(
            req.headers['AUTHORIZATION'].split(' ')[1]).decode()
        user = usps.split(':')[0]
        pswd = usps.split(':')[1]
        if(user == registered['user'] and pswd == registered['pswd']):
            at = 'xxxyyyzzz'
            issued_token.append(at)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                'access_token': at
            })
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({
                'message': 'not authorized'
            })


class ListMenuResource:
    def on_get(self, req, resp, contract_id):
        if not auth(req, resp):
            return
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(init_state['menus'])


class CheckInResource:
    def on_post(self, req, resp, contract_id):
        if not auth(req, resp):
            return
        media = req.media
        if (
            not req.media['storeId'] and
            not req.media['tables'] and
            len(req.media['tables']) > 0 and
            not req.media['number']
        ):
            resp.status = falcon.HTTP_402
            resp.body = json.dumps({
                'message': 'invalid data'
            })
            return
        res = copy.deepcopy(expect_state['check_in'])
        res['storeId'] = req.media['storeId']
        res['tables'] = req.media['tables']
        res['number'] = req.media['number']
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)


class OrderResource:
    def on_post(self, req, resp, contract_id, table_id):
        if not auth(req, resp):
            return
        media = req.media
        if (
            not req.media['items'] and
            len(req.media['items']) > 0 and
            not req.media['items'][0]['menuId'] and
            not req.media['items'][0]['quantity']
        ):
            resp.status = falcon.HTTP_402
            resp.body = json.dumps({
                'message': 'invalid data'
            })
            return
        res = copy.deepcopy(expect_state['order'])

        res['items'] = []
        for item in req.media['items']:
            if item['id'] in map(lambda item: item['id'], expect_state['order']['items']):
                for expect_item, index in enumerate(expect_state['order']['items']):
                    if item['id'] == expect_item['id']:
                        expect_item['quantity'] = item['quantity']
                        res['items'].append(expect_item)
            else:
                resp.status = falcon.HTTP_403
                resp.body = json.dumps({
                    'message': 'unknown menu'
                })
                return

        res['tableUse']['id'] = table_id
        res['tableUse']['tables'] = table_id

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)


api = falcon.API()
api.add_route('/app/{contract_id}/token', AccessResource())
api.add_route('/{contract_id}/waiter/menus', ListMenuResource())
api.add_route('/{contract_id}/waiter/table_uses', CheckInResource())
api.add_route(
    '/{contract_id}/waiter/table_uses/{table_id}/orders', OrderResource())

if __name__ == "__main__":
    httpd = simple_server.make_server("127.0.0.1", 8080, api)
    httpd.serve_forever()
