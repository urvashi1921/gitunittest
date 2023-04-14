import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_read_file(self):
        response = self.client.get('/read_file')
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.json)
