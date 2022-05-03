from selenium.webdriver.common.by import By
""" 
Файл для хранения локаторов
Набор локаторов (селекторов), применяемых на страницах сайта
"""


class MainPageLocators:
    """Локаторы главной страницы"""
    MAIN_PAGE = (By.CLASS_NAME, "wrapper")
    RUBY_LINK = (By.LINK_TEXT, "Ruby")
    MENU_OBJECT = (By.CLASS_NAME, "menu")
    MAILING_LIST_LINK = (By.LINK_TEXT, "Mailing list")
    API_DOC_LINK = (By.LINK_TEXT, "API documentation")
    SOURCE_CODE_LINK = (By.LINK_TEXT, "Source code")
    README_LINK = (By.LINK_TEXT, "README")
    CODE_OBJECT = (By.CLASS_NAME, "code")
    INSTALL_COMMAND_TEXT = (By.XPATH, "//pre[contains(text(), 'gem install capybara')]")
    ELABS_BUTTON = (By.CLASS_NAME, "elabs-symbol")

class RubyPageLocators:
    RUBY_HEADER = (By.ID, "header_content")
