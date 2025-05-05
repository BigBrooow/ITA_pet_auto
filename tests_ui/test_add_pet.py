import pytest

import generator
from client import Client
from pages.profile_page import ProfilePage


class TestAddPet:

    @pytest.mark.parametrize('pet_type', ['Dog', 'Cat'])
    def test_add_pet(self, login, pet_type):
        page = ProfilePage(login)
        page.open_page('http://34.141.58.52:8080/#/profile')
        page.click_add_pet_button()
        name = generator.random_name(5)
        page.fill_name_field(name)
        page.click_type_dropdown()
        page.click_type_item(pet_type)
        pet_id = page.get_url()
        # expected_model = PetModels()
        # Client().get_pet(pet_id, expected_model=expected_model)
