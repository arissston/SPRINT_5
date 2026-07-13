from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_redirect_to_LK_from_Main_page_by_LK_link(driver_login, new_user):
    WebDriverWait(driver_login, 5).until(
        EC.visibility_of_element_located((By.XPATH, './/button[contains(text(),"Войти")]')))

    driver_login.find_element(By.XPATH, ".//fieldset[.//label='Email']//input").send_keys(new_user["email"])
    driver_login.find_element(By.XPATH, ".//input[@type='password']").send_keys(new_user["password"])
    driver_login.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    WebDriverWait(driver_login, 5).until(
        EC.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    assert driver_login.current_url == "https://stellarburgers.education-services.ru/"

    driver_login.find_element(By.XPATH, './/a[.//p="Личный Кабинет"]').click()

    WebDriverWait(driver_login, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, ".//a[contains(@class,'link_active') and text()='Профиль']")))

    assert '/account/profile' in driver_login.current_url
