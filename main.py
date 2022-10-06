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
driver.set_window_size(width=1500, height=1040)

driver.get(url)

time.sleep(5)
driver.find_element(By.ID, 'langSelect-EN').click()
time.sleep(5)

upgrades_count = 0
products_count = 0
while True:
    time.sleep(0.1)

    second = datetime.now().second
    minute = datetime.now().minute
    hour = datetime.now().hour

    driver.find_element(By.ID, 'bigCookie').click()

    if minute % 5 == 0 and second % 60 == 0:
        # if minute % 5 == 0 and second % 60 == 0:
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

        print(f"{hour}:{minute}:{second}:: upgrades: {upgrades_count}, products: {products_count}")
