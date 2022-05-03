import allure
import pytest

from pages.locators import MainPageLocators
from pages.main_page import MainPage

main_page_link = 'http://teamcapybara.github.io/capybara/'


@allure.severity(allure.severity_level.BLOCKER)
@allure.story("Проверка отображения главной страницы")
def test_open_main_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_main_page()


@allure.story("Проверка успешного перехода по ссылке Ruby")
@allure.severity(allure.severity_level.NORMAL)
def test_get_ruby_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_ruby_link()

@allure.story("Проверка успешного перехода по объектам из меню")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.skip(reason="Не до конца разобралсась с передачей локаторов через @pytest.mark.parametrize")
@pytest.mark.parametrize("link_menu,locator_menu", [("https://groups.google.com/g/ruby-capybara", MainPageLocators.MAILING_LIST_LINK),
                                                    ("https://rubydoc.info/github/teamcapybara/capybara/master", MainPageLocators.API_DOC_LINK),
                                                    ("https://github.com/teamcapybara/capybara", MainPageLocators.SOURCE_CODE_LINK)])
def test_get_menu_link(browser, link_menu, locator_menu):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_menu(link_menu, locator_menu)

@allure.story("Проверка успешного перехода по ссылке Mailing list")
@allure.severity(allure.severity_level.NORMAL)
def test_display_menu_mailing_list(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_menu_link
    page.go_to_menu_mailing_list

@allure.story("Проверка успешного перехода по ссылке Api doc")
@allure.severity(allure.severity_level.NORMAL)
def test_display_menu_api_doc(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_menu_link
    page.go_to_menu_api_doc

@allure.story("Проверка успешного перехода по ссылке Source Code")
@allure.severity(allure.severity_level.NORMAL)
def test_display_menu_source_code(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_menu_link
    page.go_to_menu_source_code

@allure.story("Проверка успешного перехода по ссылке README")
@allure.severity(allure.severity_level.TRIVIAL)
def test_go_to_readme_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_readme_link()
