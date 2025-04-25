from typing import Optional

from pydantic import BaseModel, Field


def validate_response(response, model, status_code):
    assert response.status_code == status_code
    return model.model_validate(response.json())


class PetResponseModel(BaseModel):
    id: int


class LoginResponseModel(BaseModel):
    token: Optional[str] = None
    email: str
    id: int


class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]

