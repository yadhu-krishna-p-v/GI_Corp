from django.test import TestCase
from rest_framework.test import APIClient

class UploadCSVTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_csv_upload(self):
        with open('sample_data.csv', 'rb') as file:
            response = self.client.post('/validate-csv/', {'csv_file': file})
        self.assertEqual(response.status_code, 201)