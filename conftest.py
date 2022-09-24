import pytest
from rest_framework.test import APIClient

user_data = {
            "email": "saksham@trilogy.com",
            "password": "pass@123",
            "password1": "pass@123",
            "password2": "pass@123"
        }
content_type = 'application/json'


def get_authenticated_client(user_data):
    user_data = {
        "email": "saksham@trilogy.com",
        "password": "pass@123",
    }
    client = APIClient()
    response = client.post('/auth/login/', data=user_data, format='json')
    token = response.data.get('key')
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client


@pytest.fixture()
def signup(client, db):
    client.post('/auth/registration/', data=user_data, content_type=content_type)