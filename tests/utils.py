from rest_framework.test import APIClient


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