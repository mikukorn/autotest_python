from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE = (By.CLASS_NAME, "wrapper")
    RUBY_LINK = (By.LINK_TEXT, "Ruby")
    MAILING_LIST_LINK = (By.XPATH, ".//links[text()='Mailing list']")


class Environments():
    URL = "http://teamcapybara.github.io/capybara/"