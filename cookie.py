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
        options_btn = self.driver.find_element(By.CSS_SELECTOR, '#prefsButton .subButton')
        options_btn.click()

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
