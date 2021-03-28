import requests
import urllib
import json
from collections.abc import Iterable

debug = False


class Client:
    def __init__(self,
                 smrg_access_key_id: str, smrg_secret_access_key: str,
                 contract_id: str, scopes=[],
                 grant_type='client_credentials', scope='', development=True):
        if debug == True:
            url = "{}/app/{}/token".format('http://localhost:8080',
                                           contract_id)
            endhost = 'http://localhost:8080'
        else:
            url = "{}/app/{}/token".format('https://id.smaregi.{}'.format(
                'dev' if development else 'jp'), contract_id)
            endhost = 'https://api.smaregi.{}'.format(
                'dev' if development else 'jp')
        self._endpoint = "{}/{}/".format(endhost, contract_id)
        if len(scopes) == 0 and scope == '':
            raise Exception('no scopes!')
        params = urllib.parse.urlencode({
            'grant_type': grant_type,
            'scope': scope or ' '.join(scopes)
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(
            url=url,
            data=params,
            headers=headers,
            auth=(smrg_access_key_id, smrg_secret_access_key)
        )

        self.access_token = json.loads(r.text)['access_token']

    def list_menu(self):
        url = self._endpoint + 'waiter/menus'
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token)
        }
        r = requests.get(
            url=url,
            headers=headers,
        )
        return json.loads(r.text)

    def check_in(self, params):
        url = self._endpoint + 'waiter/table_uses'
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
        }
        r = requests.post(
            url=url,
            data=json.dumps(params),
            headers=headers
        )
        return json.loads(r.text)

    def order(self, id, params):
        url = self._endpoint + 'waiter/table_uses/' + id + '/orders'
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
        }
        r = requests.post(
            url=url,
            data=json.dumps(params),
            headers=headers
        )
        return json.loads(r.text)

