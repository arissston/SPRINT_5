from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_move_to_buns_division(driver):
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

    assert WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, ".//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']")))

    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()

    assert WebDriverWait(driver, 5).until(
             EC.visibility_of_element_located(
              (By.XPATH, ".//div[contains(@class, 'tab_type_current')]//span[text()='Булки']")))
