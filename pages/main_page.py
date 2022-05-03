import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nose.tools import assert_equal, assert_true

from .base_page import BasePage
from .locators import MainPageLocators, RubyPageLocators

menu_mailing_list_link = 'https://groups.google.com/g/ruby-capybara'
menu_api_doc_link = 'https://rubydoc.info/github/teamcapybara/capybara/master'
menu_source_code_link = 'https://github.com/teamcapybara/capybara'
readme_link = 'https://rubydoc.info/github/teamcapybara/capybara'

class MainPage(BasePage):
    def go_to_main_page(self):
        assert self.is_element_present(*MainPageLocators.MAIN_PAGE), 'Page not loaded'

    def go_to_ruby_link(self):
        self.browser.find_element(*MainPageLocators.RUBY_LINK).click()
        assert self.is_element_present(*RubyPageLocators.RUBY_HEADER), 'Page not loaded'

    def go_to_menu_link(self):
        status = self.browser.find_element(*MainPageLocators.MENU_OBJECT).is_displayed()
        if status == True:
            assert True
        else:
            allure.attach(self.browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            self.browser.close()
            assert False

    def go_to_menu(self, link_menu, locator_menu):
        wait = WebDriverWait(self.browser, 5)
        window_before = self.browser.window_handles[0]
        print(window_before)
        self.browser.find_element(locator_menu).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.url_to_be(link_menu))

    def go_to_readme_link(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.find_element(*MainPageLocators.README_LINK).click()
        wait.until(EC.url_to_be(readme_link))

    def go_to_menu_mailing_list(self, menu_mailing_list_link):
        wait = WebDriverWait(self.browser, 5)
        window_before = self.browser.window_handles[0]
        print(window_before)
        self.browser.find_element(*MainPageLocators.MAILING_LIST_LINK).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.url_to_be(menu_mailing_list_link))

    def go_to_menu_api_doc(self, menu_api_doc_link):
        wait = WebDriverWait(self.browser, 5)
        window_before = self.browser.window_handles[0]
        print(window_before)
        self.browser.find_element(*MainPageLocators.API_DOC_LINK).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.url_to_be(menu_api_doc_link))

    def go_to_menu_source_code(self, menu_source_code_link):
        wait = WebDriverWait(self.browser, 5)
        window_before = self.browser.window_handles[0]
        print(window_before)
        self.browser.find_element(*MainPageLocators.SOURCE_CODE_LINK).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.url_to_be(menu_source_code_link))

    def check_code_object_command_install(self):
        self.browser.find_element(*MainPageLocators.CODE_OBJECT)
        self.browser.find_element(*MainPageLocators.INSTALL_COMMAND_TEXT)

    def click_elabs_icon(self):
        self.browser.find_element(*MainPageLocators.ELABS_BUTTON).click()

