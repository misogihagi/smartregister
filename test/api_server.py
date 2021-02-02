from wsgiref import simple_server
import falcon
import json
import base64

registered = {
    'user': 'user',
    'pswd': 'pswd'
}
access_token = 'xxx'
contract_id = 'ccc'
table_id = 1


class AccessResource:
def on_post(self, req, resp, contract_id):


usps = base64.b64decode(req.headers['AUTHORIZATION'].split(' ')[1]).decode()
user = usps.split(':')[0]
pswd = usps.split(':')[1]
if(user == registered['user'] and pswd == registered['pswd']):
resp.status = falcon.HTTP_200
resp.body = json.dumps({
    'access_token': access_token
})
else:
resp.status = falcon.HTTP_400


class ListMenuResource:
def on_post(self, req, resp, contract_id):


params = req.stream.read().decode('utf-8')
items = {
    'title': 'WebAPI(POST)',
    'tags': [
        {
            'name': 'テスト', 'バージョン': []
        },
        {
            'name': 'request', params: []
        }
    ]
}
resp.status = falcon.HTTP_200
resp.content_type = 'text/plain'
resp.body = json.dumps(items)


class CheckInResource:
def on_post(self, req, resp, contract_id):


pass


class OrderResource:
def on_post(self, req, resp, contract_id, table_id):


pass

api = falcon.API()
api.add_route('/app/{contract_id}/token', AccessResource())
api.add_route('{contract_id}/waiter/menus', ListMenuResource())
api.add_route('{contract_id}/waiter/table_uses', ListMenuResource())
api.add_route(
    '{contract_id}/waiter/table_uses/{table_id}/orders', ListMenuResource())

if __name__ == "__main__":

httpd = simple_server.make_server("127.0.0.1", 8080, api)
httpd.serve_forever()
