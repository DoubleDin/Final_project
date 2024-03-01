import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

from base.base_class import Base
from pages.main_page import Main_page
from pages.product_filtration import Filtration_product
from pages.product_page import Product_page
from utilites.logger import Logger


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    section_word_locator = "//section[@class='catalog']/h1"
    smartphone_category_locator = "//a[@href='/Smartfony/']"
    smph_page_word_locator = "//section[@class='product-list flex-wrap']/h1"
    arrow_sort_list_locator = "//div[@class='jq-selectbox__trigger-arrow']"
    sort_price_locator = "//select[@name='ff']/option[@value='2']"

    favorite_page_button_loc = "//a[@href='/favorite/']"
    word_on_favorite_page_loc = "//section[@class='product-list']/h1"

    element_on_page_loc = "//div[@class='pad']"

    # GETTERS
    def get_section_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.section_word_locator)))

    def get_smartphone_category_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.smartphone_category_locator)))

    def get_smph_page_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.smph_page_word_locator)))

    def get_arrow_sort_list_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrow_sort_list_locator)))

    def get_sort_price_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_price_locator)))

    def get_favorite_page_button_loc(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.favorite_page_button_loc)))

    def get_favorite_page_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_on_favorite_page_loc)))

    def get_element_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.element_on_page_loc)))

    # ACTIONS

    def smartphone_category(self):
        self.get_smartphone_category_locator().click()
        print("Go to category Smartphones")

    def click_and_choose_sort_price(self):
        self.get_arrow_sort_list_locator().click()
        self.get_sort_price_locator().click()
        print("Sorting product by price")

    def favorite_page_go(self):
        self.get_favorite_page_button_loc().click()
        print("Go to Favorite Page")

    # METHODS

    def check_element_on_page(self):
        try:
            self.get_element_locator()
        except TimeoutException:
            return print("No element, page empty")
        return print("We find element")

    def go_to_category(self):
        Logger.add_start_step(method="go_to_category")
        c = Main_page(self.driver)
        c.transit_to_catalog()
        self.assert_word(self.get_section_word(), "Электроника")
        self.smartphone_category()
        self.assert_word(self.get_smph_page_word(), "Купить смартфоны в Донецке (ДНР)")
        self.click_and_choose_sort_price()
        Logger.add_end_step(url=self.driver.current_url, method="go_to_category")

    def filter_product(self):
        Logger.add_start_step(method="filter_product")
        f = Filtration_product(self.driver)
        f.activate_checkbox()
        self.check_element_on_page()
        f.add_to_favorite_and_cancel_filter()
        f.filter_price()
        self.check_element_on_page()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="filter_product")

    def filtration_for_buy_product(self):
        Logger.add_start_step(method="filtration_for_buy_product")
        f = Filtration_product(self.driver)
        f.filter_for_buy()
        self.check_element_on_page()
        Logger.add_end_step(url=self.driver.current_url, method="filtration_for_buy_product")

    def go_to_favorite(self):
        Logger.add_start_step(method="go_to_favorite")
        self.favorite_page_go()
        self.assert_url("https://e-mobi.com.ru/favorite/")
        self.assert_word(self.get_favorite_page_word(), "Избранное")
        self.check_element_on_page()
        self.get_screenshot()
        self.driver.back()
        print("Back to Filter Page")
        Logger.add_end_step(url=self.driver.current_url, method="go_to_favorite")



