from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import MainPageLocators, RubyPageLocators

mailing_list_link = 'https://groups.google.com/g/ruby-capybara'
readme_link = 'https://rubydoc.info/github/teamcapybara/capybara'

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.MAIN_PAGE), 'Page not loaded'

    def go_to_ruby_link(self):
        self.browser.find_element(*MainPageLocators.RUBY_LINK).click()
        assert self.is_element_present(*RubyPageLocators.RUBY_HEADER), 'Page not loaded'

    def go_to_menu_link(self):
        self.browser.find_element(*MainPageLocators.MENU_OBJECT).is_displayed()

    def go_to_mailing_list(self):
        wait = WebDriverWait(self.browser, 5)
        window_before = self.browser.window_handles[0]
        print(window_before)
        self.browser.find_element(*MainPageLocators.MAILING_LIST_LINK).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.url_to_be(mailing_list_link))

    def go_to_readme_link(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.find_element(*MainPageLocators.README_LINK).click()
        wait.until(EC.url_to_be(readme_link))
