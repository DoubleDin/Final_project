import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_modal(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    login_button_locator = "//a[@href='#ex1']"
    input_phone_locator = "//input[@name='aut-phone']"
    input_password_locator = "//input[@name='aut-pass']"
    button_enter_locator = "//*[@id='ex1']/form/div/button"
    login_success_locator = "//a[@href='/cabinet/']"

    # GETTERS

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_phone_locator)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password_locator)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter_locator)))

    def get_login_success_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_success_locator)))

    # ACTIONS

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    def input_phone(self, user_name):
        self.get_input_phone().click()  # Активация поля
        self.get_input_phone().send_keys(user_name)  # Ввод номера
        print("Input phone")

    def input_password(self, password):
        self.get_input_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_button_enter().click()
        print("Click Enter Button")

    # METHODS

    def authorization(self):
        # self.get_current_url()
        self.click_login_button()
        time.sleep(3)
        self.input_phone('9493421208')
        self.input_password('11qqaazz')
        self.click_enter_button()
        self.assert_word(self.get_login_success_locator(), "Di")  # Проверка авторизации пользователя
        self.get_screenshot()
