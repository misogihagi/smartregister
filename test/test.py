c = Client(
    'user',
    'pswd',
    'contract', [
        'pos.products:read',
    ])

print(c.list_menu())
[{'id': '1', 'name': 'menu1', 'kana': '', 'type': 'normal', 'categoryId': '1', 'note': '', 'sortNo': 1, 'customId': None, 'applyDatetime': None, 'isOpenPrice': False, 'createdIn': 'waiter', 'prices': [{'taxRate': 10, 'taxType': 'normal', 'amount': '0', 'tax': 'include', 'primary': True}]}, {'id': '2', 'name': 'd', 'kana': '', 'type': 'normal', 'categoryId': '1', 'note': '', 'sortNo': 2, 'customId': None, 'applyDatetime': None, 
'isOpenPrice': False, 'createdIn': 'waiter', 'prices': [{'taxRate': 10, 'taxType': 'normal', 'amount': '500', 'tax': 'include', 'primary': True}]}]
params = {
    'storeId': '1',
    'tables': [{
        'id': '1'
    }],
    'number': 1,
}
c.check_in(params)
{'id': '1', 'tables': [{'id': '1', 'name': 'T1'}], 'number': 1, 'customerGroups': [], 'status': 'started', 'started': '2021-02-03T00:43:06+09:00', 'ended': None, 'storeId': '1', 'quantity': 0, 'totalPrice': '0', 'temmpTransactionHeadId': None}
params = {
    'items':
    [{
        'menuId': '1',
        'quantity': 5
    }, {
        'menuId': '2',
        'quantity': 5
    }]}

c.order('1', params)
{'orderId': '01XXXXXYYYYYZZZZZZ', 'ordered': '2021-02-03T00:43:07+09:00', 'items': [{'id': '1', 'meenuId': '1', 'name': 'menu1', 'quantity': 5, 'status': 'waiting', 'customContentId': '', 'customContentNam'e': '', 'categoryId': '1', 'menuType': 'normal', 'memo': '', 'sellingPrice': {'taxRate': 10, 'taxType': 'noarmal', 'amount': '0', 'tax': 'included'}, 'discount': None, 'toppings': []}, {'id': '2', 'menuId': '2', 'name': 'menu2', 'quantity': 5, 'status': 'waiting', 'customContentId': '', 'customContentName': '', 'categoryId'': '1', 'menuType': 'normal', 'memo': '', 'sellingPrice': {'taxRate': 10, 'taxType': 'normal', 'amount': '44t4', 'tax': 'included'}, 'discount': None, 'toppings': []}], 'tableUse': {'id': '1', 'status': 'started', 's'toreId': '1', 'tables': [{'id': '1', 'name': 'T1'}]}}
