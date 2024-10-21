import unittest
from midterm import app

class TestMidterm(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b' is Midterm exam!')

if __name__ == '__main__':
    unittest.main()
