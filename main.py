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
driver.set_window_position(700, 0)

driver.get(url)

time.sleep(2)
driver.find_element(By.ID, 'langSelect-EN').click()
time.sleep(2)

# products = driver.find_elements(By.CSS_SELECTOR, 'div .locked')
# print(len(products))
# for product in products:
#     product_name = product.find_element(By.CLASS_NAME, 'div.title')
#     print(product_name.get_attribute("textContent"))

# product = driver.find_element(By.CSS_SELECTOR, '.unlocked .title')
# print(product.get_property('textContent'))

products = driver.find_element(By.ID, 'products').find_elements(By.CSS_SELECTOR, '.unlocked')
# print(len(products))
for product in products:
    print(product.find_element(By.CLASS_NAME, 'title').get_property('textContent'))

while True:
    time.sleep(0.25)
    second = datetime.now().second
    driver.find_element(By.ID, 'bigCookie').click()

    if second % 30:
        products = driver.find_element(By.ID, 'products').find_elements(By.CSS_SELECTOR, '.unlocked')


