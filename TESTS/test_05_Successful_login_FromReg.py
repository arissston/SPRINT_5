from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_login_from_registerpage_enterclick(driver_reg, new_user):
    driver_reg.find_element(By.XPATH, ".//a[contains(text(),'Войти')]").click()

    WebDriverWait(driver_reg, 5).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/login"))

    WebDriverWait(driver_reg, 5).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))

    driver_reg.find_element(By.XPATH, ".//fieldset[.//label='Email']//input").send_keys(new_user["email"])
    driver_reg.find_element(By.XPATH, ".//input[@type='password']").send_keys(new_user["password"])
    driver_reg.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    WebDriverWait(driver_reg, 5).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

    assert driver_reg.current_url == "https://stellarburgers.education-services.ru/"
