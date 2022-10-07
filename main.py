import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

url = "https://orteil.dashnet.org/cookieclicker/"
driver.set_window_position(400, 0)
driver.set_window_size(width=1525, height=1045)

driver.get(url)

time.sleep(5)
driver.find_element(By.ID, 'langSelect-EN').click()
time.sleep(5)

upgrades_count = 0
products_count = 0
while True:
    time.sleep(0.1)

    microseconds = datetime.now().microsecond
    second = datetime.now().second
    minute = datetime.now().minute
    hour = datetime.now().hour

    driver.find_element(By.ID, 'bigCookie').click()

    # I'll buy from the store and save the progress every 5 minutes
    if minute % 5 == 0 and second == 0 and microseconds < 100000:
        upgrades = driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')
        upgrades_count = len(upgrades)
        if len(upgrades) > 0:
            upgrades[-1].click()
            print('Upgrade bought')
        else:
            products = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
            products_count = len(products)
            if len(products) > 0:
                highest_product = products[-1]
                highest_product.click()
                print(
                    f'{highest_product.find_element(By.CSS_SELECTOR, ".title.productName").get_property("textContent")} bought')

        print(f"{hour}:{minute}:{second}:{microseconds}:: upgrades: {upgrades_count}, products: {products_count}")

        # save the game progress
        # press the options button to open the menu
        options_btn = driver.find_element(By.CSS_SELECTOR, '#prefsButton .subButton')
        options_btn.click()
        # press save to file button
        save_to_file_btn = driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[5]/a[1]')
        save_to_file_btn.click()
        print("File saved")
        # press the options button to close the menu
        options_btn = driver.find_element(By.CSS_SELECTOR, '#prefsButton .subButton')
        options_btn.click()

        print()

