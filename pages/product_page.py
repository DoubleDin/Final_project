import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    product_card_loc = "/html/body/div[1]/section[3]/div[3]/div[2]/div[1]/div/a[3]"
    name_product_loc = "//section[@class='product']/div[@class='product-name']/h1"
    art_product_loc = "/html/body/div[1]/section[3]/div[1]/div/span/b"
    price_product_loc = "/html/body/div[1]/section[3]/div[2]/div[2]/div[3]/div[1]/div[2]/price"

    next_photo_arrow_loc = "//div[@id='demo-test-gallery']/button[@class='slick-next slick-arrow']"
    prev_photo_arrow_loc = "//div[@id='demo-test-gallery']/button[@class='slick-prev slick-arrow']"

    add_to_favorite_loc = "//a[@class='add_favorite']"
    add_to_basket_loc = "//a[@class='add-to-basket']"

    basket_button_loc = "//a[@href='/basket/']/span"

    # GETTERS

    def get_product_card_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.product_card_loc)))

    def get_product_name_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.name_product_loc)))

    def get_product_art_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.art_product_loc)))

    def get_product_price_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.price_product_loc)))

    def get_next_photo_arrow_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.next_photo_arrow_loc)))

    def get_prev_photo_arrow_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.prev_photo_arrow_loc)))

    def get_add_to_favorite_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.add_to_favorite_loc)))

    def get_add_to_basket_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.add_to_basket_loc)))

    def get_basket_button_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.basket_button_loc)))

    # ACTIONS

    def click_product_card(self):
        self.get_product_card_loc().click()
        print("Click Product Card")

    def get_text(self):
        print(self.get_product_name_loc().text)
        print(self.get_product_art_loc().text)
        print(self.get_product_price_loc().text)

    def view_photo_gallery(self):
        self.get_next_photo_arrow_loc().click()
        print('Next photo')
        time.sleep(2)
        self.get_prev_photo_arrow_loc().click()
        print("Previously photo")

    def add_to_favorite(self):
        self.get_add_to_favorite_loc().click()
        print("Add product to favorite")

    def add_to_basket(self):
        self.get_add_to_basket_loc().click()
        print("Add product to basket")

    # METHODS

    def product_page(self):
        Logger.add_start_step(method="product_page")
        self.click_product_card()
        self.get_text()
        self.assert_word(self.get_product_name_loc(), '6.7" Смартфон HONOR 90 512 ГБ зеленый')
        self.assert_word(self.get_product_art_loc(), "149046")
        self.move_screen(100)
        self.view_photo_gallery()
        self.add_to_favorite()
        self.add_to_basket()
        self.assert_word(self.get_basket_button_loc(), "Корзина (1)")
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="product_page")

