from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_login_from_main_page_enter_button(driver, new_user):
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]").click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/login"))

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))

    driver.find_element(By.XPATH, ".//fieldset[.//label='Email']//input").send_keys(new_user["email"])
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(new_user["password"])
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver.current_url == "https://stellarburgers.education-services.ru/"
