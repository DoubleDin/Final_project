import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from base.base_class import Base


class Filtration_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    brand_scrollbar_locator = "//div[@id='mCSB_1_dragger_vertical']/div[@class='mCSB_dragger_bar']"
    screen_resolution_scrollbar_locator = "//div[@id='mCSB_2_dragger_vertical']/div[@class='mCSB_dragger_bar']"
    ram_scrollbar_locator = "//div[@id='mCSB_4_dragger_vertical']/div[@class='mCSB_dragger_bar']"

    apple_brand_check_locator = "//div[@class='checkbox']/label[@for='fb_ch_18']"
    google_brand_check_locator = "//div[@class ='checkbox']/label[@for='fb_ch_290']"
    honor_brand_check_locator = "//div[@class ='checkbox']/label[@for='fb_ch_29']"
    huawei_brand_check_locator = "//div[@class ='checkbox']/label[@for='fb_ch_32']"
    show_product_locator = "//span[@onclick='ShowTooltips(32)']"

    screen_diagonal_4_5_locator = "//div[@class='checkbox']/label[@for='f_ch_4596']"
    screen_diagonal_5_6_locator = "//div[@class='checkbox']/label[@for='f_ch_4597']"
    screen_diagonal_6_more_locator = "//div[@class='checkbox']/label[@for='f_ch_4598']"

    checkbox_resolution_2400_1800_loc = "//div[@class='checkbox']/label[@for='f_ch_4599']"
    checkbox_resolution_1600_720_loc = "//div[@class='checkbox']/label[@for='f_ch_4604']"
    checkbox_resolution_2412_1080_loc = "//div[@class='checkbox']/label[@for='f_ch_4627']"
    checkbox_resolution_2340_1080_loc = "//div[@class='checkbox']/label[@for='f_ch_4629']"

    material_case_metal_glass_loc = "//div[@class='checkbox']/label[@for='f_ch_4625']"
    material_case_plastic_glass_loc = "//div[@class='checkbox']/label[@for='f_ch_4634']"
    material_case_glass_loc = "//div[@class='checkbox']/label[@for='f_ch_4637']"

    os_ios_checkbox_loc = "//div[@class='checkbox']/label[@for='f_ch_4630']"

    ram_4_locator = "//div[@class='checkbox']/label[@for='f_ch_8003']"

    rom_256_locator = "//div[@class='checkbox']/label[@for='f_ch_4603']"

    apply_filter_button_loc = "//a[@class='apply-filters']"

    add_to_favorite_loc = "//a[@data-id='155580']"

    cancel_filter_button_loc = "//a[@class='cansel']"

    from_price_input_loc = "//input[@class='fprice-ot']"
    to_price_input_loc = "//input[@class='fprice-do']"

    # GETTERS
    def get_brand_scroll_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.brand_scrollbar_locator)))

    def get_screen_resolution_scroll_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.screen_resolution_scrollbar_locator)))

    def get_ram_scroll_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.ram_scrollbar_locator)))

    def get_apple_brand_check_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.apple_brand_check_locator)))

    def get_google_brand_check_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.google_brand_check_locator)))

    def get_honor_brand_check_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.honor_brand_check_locator)))

    def get_huawei_brand_check_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.huawei_brand_check_locator)))

    def get_show_product_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.show_product_locator)))

    def get_screen_diagonal_4_5_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.screen_diagonal_4_5_locator)))

    def get_screen_diagonal_5_6_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.screen_diagonal_5_6_locator)))

    def get_screen_diagonal_6_more_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.screen_diagonal_6_more_locator)))

    def get_checkbox_resolution_2400_1800_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.checkbox_resolution_2400_1800_loc)))

    def get_checkbox_resolution_1600_720_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.checkbox_resolution_1600_720_loc)))

    def get_checkbox_resolution_2412_1080_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.checkbox_resolution_2412_1080_loc)))

    def get_checkbox_resolution_2340_1080_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.checkbox_resolution_2340_1080_loc)))

    def get_material_case_metal_glass_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.material_case_metal_glass_loc)))

    def get_material_case_plastic_glass_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.material_case_plastic_glass_loc)))

    def get_material_case_glass_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.material_case_glass_loc)))

    def get_os_ios_checkbox_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.os_ios_checkbox_loc)))

    def get_ram_4_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.ram_4_locator)))

    def get_rom_256_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.rom_256_locator)))

    def get_apply_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.apply_filter_button_loc)))

    def get_add_to_favorite_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.add_to_favorite_loc)))

    def get_cancel_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.cancel_filter_button_loc)))

    def get_from_price_input_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.from_price_input_loc)))

    def get_to_price_input_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.to_price_input_loc)))

    # ACTIONS

    def move_scrollbar(self, scroll_bar):
        move = ActionChains(self.driver)
        move.click_and_hold(scroll_bar).move_by_offset(0, 30).release().perform()

    def apple_brand_check(self):
        self.get_apple_brand_check_locator().click()
        print("Check Apple Brand")

    def google_brand_check(self):
        self.get_google_brand_check_locator().click()
        print("Check Google Brand")

    def honor_brand_check(self):
        self.get_honor_brand_check_locator().click()
        print("Check Honor Brand")

    def huawei_brand_check_and_click_show(self):
        self.get_huawei_brand_check_locator().click()
        print("Check Huawei Brand")
        self.get_show_product_locator().click()
        print("Click Show Product")

    def screen_diagonal_4_5_check(self):
        self.get_screen_diagonal_4_5_locator().click()
        print("Check 4-5 diagonal")

    def screen_diagonal_5_6_check(self):
        self.get_screen_diagonal_5_6_locator().click()
        print("Check 5-6 diagonal")

    def screen_diagonal_6_more_check(self):
        self.get_screen_diagonal_6_more_locator().click()
        print("Check 6 and more diagonal")

    def checkbox_resolution_2400_1800(self):
        self.get_checkbox_resolution_2400_1800_loc().click()
        print("Check checkbox resolution 2400x1800")

    def checkbox_resolution_1600_720(self):
        self.get_checkbox_resolution_1600_720_loc().click()
        print("Check checkbox resolution 1600x720")

    def checkbox_resolution_2412_1080(self):
        self.get_checkbox_resolution_2412_1080_loc().click()
        print("Check checkbox resolution 2412x1080")

    def checkbox_resolution_2340_1080(self):
        self.get_checkbox_resolution_2340_1080_loc().click()
        print("Check checkbox resolution 2340x1080")

    def checkbox_material_case_metal_glass(self):
        self.get_material_case_metal_glass_loc().click()
        print("Check checkbox material case metal glass")

    def checkbox_material_case_plastic_glass(self):
        self.get_material_case_plastic_glass_loc().click()
        print("Check checkbox material case plastic glass")

    def checkbox_material_case_glass(self):
        self.get_material_case_glass_loc().click()
        print("Check checkbox material case glass")

    def checkbox_ios_os(self):
        self.get_os_ios_checkbox_loc().click()
        print("Check checkbox iOS os")

    def checkbox_4_ram(self):
        self.get_ram_4_locator().click()
        print("Check checkbox 4 GB RAM")

    def checkbox_256_rom(self):
        self.get_rom_256_locator().click()
        print("Check checkbox 256 GB ROM")

    def apply_filter(self):
        self.get_apply_filter_button().click()
        print("Click Apply Filter")

    def add_to_favorite(self):
        self.get_add_to_favorite_loc().click()
        print("Click favorite button")

    def cancel_filter(self):
        self.get_cancel_filter_button().click()
        print("Click cancel button")

    def price_filter(self):
        self.get_from_price_input_loc().send_keys("40000")
        self.get_to_price_input_loc().send_keys("50000")
        print("Input price limited")

    # METHODS
    def activate_checkbox(self):
        self.apple_brand_check()
        self.move_scrollbar(self.get_brand_scroll_locator())
        self.google_brand_check()
        self.move_scrollbar(self.get_brand_scroll_locator())
        self.honor_brand_check()
        self.huawei_brand_check_and_click_show()
        time.sleep(2)
        self.screen_diagonal_4_5_check()
        self.move_screen(0)
        self.screen_diagonal_5_6_check()
        self.screen_diagonal_6_more_check()
        self.move_screen(300)
        time.sleep(2)
        self.checkbox_resolution_2400_1800()
        self.checkbox_resolution_1600_720()
        self.move_scrollbar(self.get_screen_resolution_scroll_locator())
        self.checkbox_resolution_2412_1080()
        self.checkbox_resolution_2340_1080()
        time.sleep(2)
        self.checkbox_material_case_metal_glass()
        self.checkbox_material_case_plastic_glass()
        self.checkbox_material_case_glass()
        self.move_screen(900)
        time.sleep(2)
        self.checkbox_ios_os()
        self.move_scrollbar(self.get_ram_scroll_locator())
        self.checkbox_4_ram()
        self.move_screen(1300)
        self.checkbox_256_rom()
        self.apply_filter()

    def add_to_favorite_and_cancel_filter(self):
        self.add_to_favorite()
        time.sleep(2)
        self.cancel_filter()

    def filter_price(self):
        time.sleep(2)
        self.move_screen(1400)
        self.price_filter()
        self.apply_filter()

    def filter_for_buy(self):
        self.move_scrollbar(self.get_brand_scroll_locator())
        self.honor_brand_check()
        self.apply_filter()

