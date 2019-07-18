from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
import json

PASSWORD = 'pAssw0rd!'


class UserTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_can_sign_up(self):
        response = self.client.post(reverse('registration'), json.dumps({
            "displayName": "j_dawg",
            "firstName": "Jarrett",
            "lastName": "Kong",
            "active": "True",
            "countryOfOrigin": "Mars",
            "password": "password",
            "passwordConfirmation": "password"
        }), content_type='application/json')

        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        # Response data reflects the user sent back from the database
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['is_active'], user.is_active)
        self.assertEqual(response.data['country_of_origin'], user.country_of_origin)
