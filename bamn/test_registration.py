from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urls
from helpers import generate_email, generate_password
from locators import LoginPageLocators, RegistrationPageLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(urls.REGISTER_PAGE_URL)
        new_mail = generate_email()
        new_password = generate_password()

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Аристон")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(new_mail)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        assert driver.current_url == urls.LOGIN_PAGE_URL

    def test_failed_registration_after_short_password(self, driver):
        driver.get(urls.REGISTER_PAGE_URL)
        new_mail = generate_email()
        new_password = generate_password(3)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Аристон")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(new_mail)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))

        assert error.text == 'Некорректный пароль'
