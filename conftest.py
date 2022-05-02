import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\quit browser..")
    browser.quit()