
import requests
import urllib

# 任意のurl(エンドポイント)
url = 'https://id.smaregi.dev/app/${contract_id}/token'

# 送信するパラメータ(例)
params = {
    'grant_type': 'client_credentials',
    'scope':
        'pos.products:read'+
        ' waiter.stores:read'+
        ' waiter.menus:read' +
        ' waiter.orders:read'+
        ' waiter.orders:write'
    
}

# URLをエンコード
params = urllib.parse.urlencode(params)

# headerでコンテンツタイプを指定
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

# authにBasic認証のIDとPASSを設定する
r = requests.post(url=url, data=params, headers=headers, 
    auth=(client_id, client_pass)
import json
at=json.loads(r.text)['access_token']
url = 'https://api.smaregi.dev/${contract_id}//waiter/menus'
req = urllib.request.Request(url)
req.add_header('Authorization', 'Bearer '+at)

url = 'https://api.smaregi.dev/${contract_id}/waiter/table_uses/'
	
params={
'storeId':'1',
'tables':[{
    'id':'1'
}],
'number':1,
}
headers = {
    'Authorization': 'Bearer '+at,
    'Content-Type': 'application/json'
    }

r = requests.post(url=url, data=json.dumps(params), headers=headers) 
print(r.text)

url = 'https://api.smaregi.dev/${contract_id}/waiter/table_uses/1/orders'
params={
    'items':
    [{
  'menuId':'1',
  'quantity':5
},{
  'menuId':'2',
  'quantity':5
}]}
headers = {
    'Authorization': 'Bearer '+at,
    'Content-Type': 'application/json'
    }

r = requests.post(url=url, data=json.dumps(params), headers=headers) 
print(r.text)

