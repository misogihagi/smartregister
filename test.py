import unittest
import sys
import yaml
from beluga import Client

try:
    with open('test/expect_state.yaml') as file:
        expect_state = yaml.safe_load(file)
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)


class TestBeruga(unittest.TestCase):
  def __init__(self):
    self.client=Client(
      expect_state['access'][0]['username'],
      expect_state['access'][0]['password'],
      scopes= ['access'][0]
    )

    
  def test_list_menu(self):
    self.assertEqual(expect_state['menus'], self.client.list_menu())

  def test_check_in(self):
    params = {
      'storeId': '1',
      'tables': [{
          'id': '1'
      }],
      'number': 1,
    }
    result=self.client.check_in(params)
    self.store=result['storeId']
    self.assertEqual(expect_state['menus'], result)

  def test_check_in(self):
    params = {
      'items':
      [{
          'menuId': '1',
          'quantity': 5
      }, {
          'menuId': '2',
          'quantity': 5
      }]
    }
    self.assertEqual(expect_state['menus'], self.client.order(self.store, params))

if __name__ == "__main__":
    unittest.main()

