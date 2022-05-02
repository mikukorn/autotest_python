from selenium.webdriver.common.by import By
""" 
Файл для хранения локаторов
Набор локаторов (селекторов), применяемых на страницах сайта
"""


class MainPageLocators:
    """Локаторы хэдэра"""
    MAIN_PAGE = (By.CLASS_NAME, "wrapper")
    RUBY_LINK = (By.LINK_TEXT, "Ruby")
    MENU_OBJECT = (By.CLASS_NAME, "menu")
    MAILING_LIST_LINK = (By.LINK_TEXT, "Mailing list")
    API_DOC_LINK = (By.LINK_TEXT, "API documentation")
    SOURCE_CODE_LINK = (By.LINK_TEXT, "Source code")
    README_LINK = (By.LINK_TEXT, "README")

class RubyPageLocators:
    RUBY_HEADER = (By.ID, "header_content")
