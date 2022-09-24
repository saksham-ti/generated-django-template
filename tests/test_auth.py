import pytest

from .utils import get_authenticated_client

user_data = {
            "email": "saksham@trilogy.com",
            "password1": "pass@123",
            "password2": "pass@123"
        }
content_type = 'application/json'

@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db

    def test_signup(self, client, db):
        response = client.post('/auth/registration/', data=user_data, content_type=content_type)
        assert response.status_code == 201
        assert "key" in response.data

    def test_login(self, client, signup):
        user_data = {
            "email": "saksham@trilogy.com",
            "password": "pass@123",
        }
        response = client.post('/auth/login/', data=user_data, content_type=content_type)
        assert response.status_code == 200
        assert 'key' in response.data

    def test_login_fail(self, client):
        response = client.post('/auth/login/', data=user_data, content_type=content_type)
        assert response.status_code == 400

    def test_logout(self, client, django_user_model, signup):
        client = get_authenticated_client(user_data)
        response = client.post('/auth/logout/', content_type=content_type)
        assert response.status_code == 200
