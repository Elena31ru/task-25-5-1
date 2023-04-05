from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(browser):
    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert result == "PetFriends", "login error"


def test_pets_cards(browser):
    images = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_card(browser, login):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, 'navbarNav')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.card-deck')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button.btn.btn-outline-secondary')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'h1.text-center')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a.navbar-brand.header2')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/my_pets"]')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/all_pets"]')
        )
    )

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.text-center:nth-child(2)')
        )
    )
