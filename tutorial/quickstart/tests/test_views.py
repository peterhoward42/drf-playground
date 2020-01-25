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
        #assert_drf_response_status_code(response, status.HTTP_200_OK)
        response_json = response.json()
        assert response_json["count"] == 1
        assert len(response_json["results"][0]["username"]) == 'admin'
