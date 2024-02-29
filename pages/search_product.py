import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from base.base_class import Base


class Search_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    search_input_locator = "//input[@name='q']"
    button_search_locator = "//div[@class='search flex']/button[@type='submit']"

    # GETTERS

    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_input_locator)))

    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search_locator)))

    # ACTIONS

    def search_input(self, word):
        self.get_search_input().send_keys(word)
        print("Fill input Search")

    def click_search_button(self):
        self.get_button_search().click()
        print("Click Search Button")

    # METHODS
    def search_product(self):
        self.search_input('Iphone 11')
        self.click_search_button()
        self.assert_url('https://e-mobi.com.ru/search/?q=Iphone+11')
        self.get_screenshot()

