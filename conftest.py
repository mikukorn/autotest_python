import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\start browser Chrome for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\quit browser..")
    browser.quit()