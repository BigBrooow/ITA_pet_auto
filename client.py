import allure
import requests

from allure_helper import AllureHelper
from models.pet_models import LoginModel, validate_response, LoginResponseModel


class ClientApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'
        self.session = self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                json):
        response = self.session.request(
            method=method,
            url=self.base_url+url,
            json=json
        )
        return response


class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self,
              request: LoginModel,
              expected_model=LoginResponseModel,
              status_code: int = 200):
        response = self.request(
            method='post',
            url='login',
            json=request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('GET /pet/{id}')
    def get_pet(self,
                pet_id: int,
                request,
                expected_model,
                status_code: int = 200
                ):
        response = self.request(
            method='get',
            url=f'pet/{pet_id}',
            json=request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)