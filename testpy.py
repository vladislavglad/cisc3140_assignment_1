from app import app
import unittest

//not needed; instead use print('hi')
class testapp(unittest.TestCase):

    def test_home(self):
        test = app.test_client(self)
        response = test.get('/')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
