from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urls
from locators import (ForgotPasswordPageLocators, LoginPageLocators,
                      MainPageLocators, RegistrationPageLocators)


class TestLogin:

    def test_successful_login_from_main_page_enter_button(self, driver, new_user):
        driver.get(urls.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(urls.LOGIN_PAGE_URL))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL

    def test_successful_login_from_main_page_LK_text_link(self, driver, new_user):
        driver.get(urls.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(urls.LOGIN_PAGE_URL))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL

    def test_successful_login_from_registerpage_enterclick(self, driver, new_user):
        driver.get(urls.REGISTER_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(urls.LOGIN_PAGE_URL))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL

    def test_successful_login_from_forgotpage_enterclick(self, driver, new_user):
        driver.get(urls.FORGOT_PASSWORD_PAGE_URL)
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(urls.LOGIN_PAGE_URL))

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL
