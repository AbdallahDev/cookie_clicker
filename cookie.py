import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class Cookie:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        self.set_window()
        self.get_website()
        self.select_language()
        self.load_file()
        self.gameplay()

    def set_window(self):
        self.driver.set_window_position(400, 0)
        self.driver.set_window_size(width=1525, height=1045)

    def get_website(self):
        url = "https://orteil.dashnet.org/cookieclicker/"
        self.driver.get(url)

    def select_language(self):
        time.sleep(5)
        self.driver.find_element(By.ID, 'langSelect-EN').click()
        time.sleep(5)

    def time_to_act(self):
        microseconds = datetime.now().microsecond
        second = datetime.now().second
        minute = datetime.now().minute
        hour = datetime.now().hour

        if minute % 5 == 0 and second == 0 and microseconds < 100000:
            # print time of the action
            print(
                f"{hour}:{minute}:{second}:{microseconds}")
            return True

    def buy_upgrade(self):
        upgrades = self.driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')
        upgrades_count = len(upgrades)
        if len(upgrades) > 0:
            # click the most efficient upgrade
            upgrades[-1].click()
            print('Upgrade bought')
            time.sleep(0.1)

    def buy_product(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
        products_total = len(products)
        if len(products) > 0:
            highest_product = products[-1]
            highest_product.click()
            print(
                f'{highest_product.find_element(By.CSS_SELECTOR, ".title.productName").get_property("textContent")} '
                f'bought')
            time.sleep(0.1)

    def save_to_file(self):
        # save the game progress
        # press the options button to open the menu
        options_btn = self.driver.find_element(By.CSS_SELECTOR, '#prefsButton .subButton')
        options_btn.click()
        # press save to file button
        save_to_file_btn = self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[5]/a[1]')
        save_to_file_btn.click()
        print("File saved")

        # press the options button to close the menu
        options_btn.click()

        time.sleep(0.1)

    def load_file(self):
        # time.sleep(20)
        # press the options button to open the menu
        options_btn = self.driver.find_element(By.CSS_SELECTOR, '#prefsButton .subButton')
        options_btn.click()

        load_file_btn = self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[5]/a[2]')
        load_file_btn.click()

        options_btn.click()

        time.sleep(10)

    def gameplay(self):
        print("GamePlay started :-)")
        while True:
            self.driver.find_element(By.ID, 'bigCookie').click()

            # I'll buy from the store and save the progress every 5 minutes
            if self.time_to_act():
                self.buy_upgrade()
                self.buy_product()
                self.save_to_file()

                print()

# todo accept the website cookies
