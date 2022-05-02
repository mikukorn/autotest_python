from pages.main_page import MainPage
from pages.locators import Environments


def test_guest_can_go_to_login_page(browser):
    link = Environments.URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()