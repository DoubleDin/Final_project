import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from base.base_class import Base
from pages.login_modal_window import Login_modal
from pages.search_product import Search_product


class Main_page(Base):
    url = 'https://e-mobi.com.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    popular_section_locator = "//section[@class='pupular-category']/h3[@class='head-title']"
    category_locator = "//a[@href='/Smartfony/']"
    logo_locator = "//a[@href='/']"
    top_rating_locator = "//section[@class='top-rating']/h3[@class='head-title']"
    arrow_next_locator = "//div[@class='top-rating-list slider-items slick-initialized slick-slider']/button[@aria-label='Next']"
    arrow_prev_locator = "//div[@class='top-rating-list slider-items slick-initialized slick-slider']/button[@aria-label='Previous']"
    catalog_electronics_locator = "//a[@href='Elektronika/']"

    # GETTERS

    def get_popular_section_locator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popular_section_locator)))

    def get_category_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_locator)))

    def get_logo_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_locator)))

    def get_top_rating_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.top_rating_locator)))

    def get_arrow_next_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrow_next_locator)))

    def get_arrow_prev_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrow_prev_locator)))

    def get_catalog_electronics_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_electronics_locator)))

    # ACTIONS

    # Поиск блока и вывод его названия на печать
    def find_popular_section(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_popular_section_locator())
        print(self.get_popular_section_locator().text)

    # Выбор и клик по выбранной категории
    def click_category(self):
        self.get_category_locator().click()
        print("Click Category")

    # Возвращение на главную страницу через клик по логотипу
    def back_to_main_page(self):
        self.get_logo_button().click()
        print("Go Main Page")

    # Поиск блока и вывод его названия на печать
    def find_top_rating(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_top_rating_locator())
        print(self.get_top_rating_locator().text)

    # Клик на стрелку вперед
    def click_arrow_next(self):
        self.get_arrow_next_locator().click()
        print("Click Arrow Next")

    # Клик на стрелку назад
    def click_arrow_prev(self):
        self.get_arrow_prev_locator().click()
        print("Click Arrow Prev")

    def click_catalog_electronics(self):
        self.get_catalog_electronics_locator().click()
        print("Click Electronic Category")

    # METHODS

    # Авторизация на главной
    def main_authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        log = Login_modal(self.driver)
        log.authorization()

    # Поиск товара в поисковой строке и переход на страницу поиска
    def searching(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        s = Search_product(self.driver)
        s.search_product()
        self.back_to_main_page()  # Возвращаемя на главную страницу
        self.assert_url('https://e-mobi.com.ru/')  # Проверяем, что вернулись на главную

    # Переход к блоку популярных категорий, выбор категории и переход в нее
    def choice_popular_category(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.find_popular_section()
        self.click_category()
        self.assert_url("https://e-mobi.com.ru/Smartfony/")
        self.back_to_main_page()  # Возвращаемя на главную страницу

    # Блок с популярными товарами(Новинки), пролистывание товаров вперед/назад
    def top_rating_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.find_top_rating()
        self.click_arrow_next()
        time.sleep(2)
        self.click_arrow_prev()

    def transit_to_catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_catalog_electronics()
        self.get_current_url()

