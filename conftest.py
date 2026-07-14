import pytest
import requests
from selenium import webdriver

import urls
from helpers import generate_email, generate_password


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def new_user():

    email = generate_email()
    password = generate_password()
    response = requests.post(
        urls.API_REGISTER_URL,
        json={"email": email, "password": password, "name": "Аристон"},
        timeout=10)

    response.raise_for_status()
    return {"email": email, "password": password}
