import pytest

from api import PetsApi
from client import Client
from config import LoginPageConfig
from models.pet_models import PetResponseModel, validate_response, LoginResponseModel, LoginModel


class TestApi:

    def test_login_api(self):
        Client().login(request=LoginModel(
            email=LoginPageConfig().EMAIL,
            password=LoginPageConfig().PASSWORD
        ), expected_model=LoginResponseModel(
            email=LoginPageConfig().EMAIL,
            id=1158
        ))

    def test_post_pet(self):
        response = PetsApi().post_pet('a', 'a', 1, 'A')
        status_code = response[1]
        expected_model = PetResponseModel()
        assert status_code == 200
        assert type(response[0]['id']) is int


class TestApiNegative:

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, password):
        res = PetsApi().login(LoginPageConfig.EMAIL, '')
        status_code = res[1]
        assert status_code == 400
        assert res[0]['detail'] == 'Username is taken or pass issue'
