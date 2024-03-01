import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites.logger import Logger


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    basket_button_total_loc = "//span[@href='/basket/']"

    page_word_basket_loc = "//section[@class='basket newBasket flex-wrap']/h1"

    name_product_basket_loc = "//a[@class='product-name']"
    price_product_basket_loc = "//price[@data-id='50710']"

    counter_plus_loc = "/html/body/div[1]/section[3]/div/div[1]/div/div/div/span[2]"
    counter_minus_loc = "/html/body/div[1]/section[3]/div/div[1]/div/div/div/span[1]"

    delete_button_loc = "//a[@class='product-del']"

    empty_basket_text_loc = "//span[@class='empty_basket']"

    # GETTERS

    def get_basket_button_total_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.basket_button_total_loc)))

    def get_page_word_basket_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.page_word_basket_loc)))

    def get_name_product_basket_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.name_product_basket_loc)))

    def get_price_product_basket_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.price_product_basket_loc)))

    def get_counter_plus_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.counter_plus_loc)))

    def get_counter_minus_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.counter_minus_loc)))

    def get_button_delete_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.delete_button_loc)))

    def get_empty_basket_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.empty_basket_text_loc)))

    # ACTIONS

    def go_to_basket(self):
        self.get_basket_button_total_loc().click()
        print("Click Basket Button")

    def information_product_on_basket(self):
        name = self.get_name_product_basket_loc().text
        print(name)
        price = self.get_price_product_basket_loc().text
        print(price)

    def click_counter(self):
        self.get_counter_plus_loc().click()
        print("Click plus")
        time.sleep(2)
        self.get_counter_minus_loc().click()
        print("Click minus")
        time.sleep(2)

    def delete_product(self):
        self.get_button_delete_loc().click()
        print("Delete button click")
        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept()
        time.sleep(2)
        empty_basket = self.get_empty_basket_text().text
        assert empty_basket == "В корзине пока нет товаров!"
        print("Product deleted success")

    # METHODS

    def basket_page(self):
        Logger.add_start_step(method="basket_page")
        self.go_to_basket()
        self.assert_url('https://e-mobi.com.ru/basket/')
        self.assert_word(self.get_page_word_basket_loc(), "Корзина")
        self.information_product_on_basket()
        self.assert_word(self.get_name_product_basket_loc(), '6.7" Смартфон HONOR 90 512 ГБ зеленый')
        self.assert_word(self.get_price_product_basket_loc(), "50710")
        self.click_counter()
        self.delete_product()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="basket_page")
