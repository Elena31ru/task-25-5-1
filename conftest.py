import os
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


EMAIL = os.environ.get('EMAIL', "")
PASSWORD = os.environ.get('PASSWORD', "")

BASE_URL = "https://petfriends.skillfactory.ru/"


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login(browser):
    browser.implicitly_wait(10)
    browser.get(BASE_URL)
    btn_new_user = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    btn_new_user.click()

    btn_exist_acc = browser.find_element(By.CSS_SELECTOR, "a[href='/login']")
    btn_exist_acc.click()

    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(EMAIL)

    field_pass = browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(PASSWORD)

    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()
    sleep(3)
    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    return result
