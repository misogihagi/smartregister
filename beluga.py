mport requests
import urllib
import json

class Client:
def __init__(self, smrg_access_key_id, smrg_secret_access_key, contract_id, grant_type='client_credentials', scopes, scope,debug=true):
self._endpoint = "https://id.smaregi.{}/{}/".format('dev' if debug else 'jp', contract_id)
url = "https://id.smaregi.{}/app/{}/token".format('dev' if debug else 'jp', contract_id)
params = urllib.parse.urlencode({
'grant_type': grant_type,
'scope': scope or ' '.join(scopes)
})
headers = {
'Content-Type': 'application/x-www-form-urlencoded'
}
r = requests.post(url=url, data=params, headers=headers,
auth=(smrg_access_key_id, smrg_secret_access_key)

self.access_token = json.loads(r.text)['access_token']

def list_menu:

url = self._endpoint + 'waiter/menus'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer '+at)
