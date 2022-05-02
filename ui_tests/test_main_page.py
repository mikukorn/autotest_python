import pytest
from pages.main_page import MainPage

main_page_link = 'http://teamcapybara.github.io/capybara/'

"""Check correct display of pages and elements"""
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_login_page()

"""Check correct get link Ruby"""
def test_get_ruby_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_ruby_link()

"""Check correct get link Mailing list"""
def test_get_menu_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_mailing_list()

"""Check correct display Menu"""
def test_display_menu(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_menu_link()

"""Check correct get link README"""
def test_go_to_readme_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_readme_link()
