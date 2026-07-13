from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_email, generate_password


def test_succesful_registration(driver_reg):
    new_mail = generate_email()
    new_password = generate_password()

    driver_reg.find_element(By.XPATH, ".//fieldset[.//label='Имя']//input").send_keys("Аристон")
    driver_reg.find_element(By.XPATH, ".//fieldset[.//label='Email']//input").send_keys(new_mail)
    driver_reg.find_element(By.XPATH, ".//input[@type='password']").send_keys(new_password)
    driver_reg.find_element(By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]").click()

    WebDriverWait(driver_reg, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, ".//button[contains(text(),'Войти')]")))

    assert driver_reg.current_url == 'https://stellarburgers.education-services.ru/login'
