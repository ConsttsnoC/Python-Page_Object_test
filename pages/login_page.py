from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        is_correct_url = "login" in self.browser.current_url
        assert is_correct_url, "The current url is incorrect."

    def should_be_login_form(self):
        is_login_form_exists = self.is_element_present(
            *LoginPageLocators.LOGIN_FORM)
        assert is_login_form_exists, 'Error find login form.'

    def should_be_register_form(self):
        is_register_form_exists = self.is_element_present(
            *LoginPageLocators.REGISTER_FORM)
        assert is_register_form_exists, 'Error find register form.'

    def register_new_user(self, email, password):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM)

        input_field_1 = self.browser.find_element(
            *LoginPageLocators.REG_EMAIL_FIELD)
        input_field_1.send_keys(email)

        input_field_2 = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD_1_FIELD)
        input_field_2.send_keys(password)

        input_field_3 = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD_2_FIELD)
        input_field_3.send_keys(password)

        reg_submit_button = self.browser.find_element(
            *LoginPageLocators.REG_SUBMIT_BUTTON)
        reg_submit_button.click()