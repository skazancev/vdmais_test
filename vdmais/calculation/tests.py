import json

from django.urls import reverse
from rest_framework.test import APITestCase


class CalcTestCase(APITestCase):
    def test_calculate(self):
        data = [
            {
                'clients': 20,
                'systems': 500,
                'cores': '2gb'
            },
            {
                'clients': 35,
                'systems': 1000,
                'cores': '8gb'
            }
        ]
        response = self.client.post(
            reverse('api-v1:calculation:calc-list'),
            data=data,
            format='json'
        )
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, {'total': 11697.63})
