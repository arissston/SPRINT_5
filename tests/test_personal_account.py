from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import urls
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators


class TestPersonalAccount:

    def test_successful_redirect_to_LK_from_Main_page_by_LK_link(self, driver, new_user):
        driver.get(urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TITLE))

        assert urls.PROFILE_PAGE_PATH in driver.current_url

    def test_successful_redirect_from_LK_to_Main_page_by_Konstruktor_link(self, driver, new_user):
        driver.get(urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TITLE))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL

    def test_successful_redirect_from_LK_to_Main_page_by_logo_click(self, driver, new_user):
        driver.get(urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TITLE))

        driver.find_element(*MainPageLocators.LOGO).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert driver.current_url == urls.MAIN_PAGE_URL

    def test_successful_logout_from_LK_by_Exit_link_click(self, driver, new_user):
        driver.get(urls.LOGIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TITLE))

        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        assert driver.current_url == urls.LOGIN_PAGE_URL
