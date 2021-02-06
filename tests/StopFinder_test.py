import unittest
import dingapi

class TestStopFinder(unittest.TestCase):
    def setUp(self):
        self.api = dingapi.dingapi()

    def tearDown(self):
        self.api = None
    
    def test_response_not_empty(self):
        response = self.api.stop_finder_request('ulm hbf')
        self.assertFalse(response == '')

if __name__ == '__main__':
    unittest.main()