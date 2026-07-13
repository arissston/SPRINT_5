import pytest
import requests
from selenium import webdriver
from helpers import generate_email, generate_password

BURGERS = "https://stellarburgers.education-services.ru/"
BURGERS_REG = "https://stellarburgers.education-services.ru/register"
BURGERS_FORGOT = "https://stellarburgers.education-services.ru/forgot-password"
BURGERS_LOGIN = "https://stellarburgers.education-services.ru/login"

API_REGISTER = "https://stellarburgers.education-services.ru/api/auth/register"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver(browser):
    browser.get(BURGERS)
    return browser


@pytest.fixture
def driver_reg(browser):
    browser.get(BURGERS_REG)
    return browser


@pytest.fixture
def driver_forgot(browser):
    browser.get(BURGERS_FORGOT)
    return browser


@pytest.fixture
def driver_login(browser):
    browser.get(BURGERS_LOGIN)
    return browser


@pytest.fixture
def new_user():
    email = generate_email()
    password = generate_password()
    response = requests.post(API_REGISTER, json={"email": email, "password": password, "name": "Аристон"})
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    return {"email": email, "password": password}
