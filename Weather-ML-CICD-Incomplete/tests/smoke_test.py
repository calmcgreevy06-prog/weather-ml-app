import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# tests a success in running the application
	def test_prediction_route_success(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	# tests that a form is rendered
	def test_get_form(self):
		response = self.client.get('/')
		self.assertIn(b'<form', response.data)
		self.assertIn(b'Weather Classification', response.data)
		
if __name__ == '__main__':
	unittest.main()
