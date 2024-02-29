import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """"Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    """"Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """"Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Диана\\PycharmProjects\\Final_project\\screen\\' + name_screenshot)
        print("SCREENSHOT")

    """"Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good URL")

    """"Method move screen"""

    def move_screen(self, n):
        move = n + 300
        self.driver.execute_script(f"window.scrollTo(0, {move})")
