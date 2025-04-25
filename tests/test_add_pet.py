import pytest

import generator
from pages.profile_page import ProfilePage


class TestAddPet:

    @pytest.mark.parametrize('pet_type', ['Dog', 'Cat'])
    def test_add_pet(self, login, pet_type):
        page = ProfilePage(login)
        page.open_page('http://34.141.58.52:8080/#/profile')
        page.click_add_pet_button()
        page.fill_name_field(generator.random_name(5))
        page.click_type_dropdown()
        page.click_type_item(pet_type)
