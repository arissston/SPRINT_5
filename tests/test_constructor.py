from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urls
from locators import ConstructorPageLocators


class TestConstructor:

    def test_successful_move_to_buns_division(self, driver):
        # Таб «Булки» активен по умолчанию, поэтому сначала уходим
        # на «Соусы», а затем проверяем возврат на «Булки».
        driver.get(urls.MAIN_PAGE_URL)
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_ACTIVE_TAB))

        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_ACTIVE_TAB))

    def test_successful_move_to_sauces_division(self, driver):
        driver.get(urls.MAIN_PAGE_URL)
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_ACTIVE_TAB))

    def test_successful_move_to_fillings_division(self, driver):
        driver.get(urls.MAIN_PAGE_URL)
        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_ACTIVE_TAB))
