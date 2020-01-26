from django.urls import reverse
from rest_framework.test import APITestCase

class TestView(APITestCase):

    def setUp(self):
	    print('XXXXXX setUp')

    def test_something(self):
        url = reverse("user-list")
        response = self.client.get(
            url, {"nosuchparam": "unused"}, format="json"
        )
        assert response.status_code == 200
        # response_json = response.json()
