from playwright.sync_api import expect

from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page, timeout=5000):
        super().__init__(page, timeout)
        self.ADD_PET_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
        self.NAME_FIELD = self.page.locator('//*[@id="name"]')
        self.TYPE_DROPDOWN = self.page.get_by_text('Select a Type')
        self.DELETE_BUTTON = self.page.get_by_text('Delete')

    def click_add_pet_button(self):
        self.ADD_PET_BUTTON.click(timeout=self.timeout)

    def fill_name_field(self, name):
        self.NAME_FIELD.fill(name, timeout=self.timeout)

    def click_type_item(self, pet_type):
        self.page.get_by_text(pet_type).click()

    def click_type_dropdown(self):
        self.TYPE_DROPDOWN.click()

