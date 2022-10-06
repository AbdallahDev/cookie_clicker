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
driver.get(url)

driver.implicitly_wait(20)
print(driver.find_element(By.ID, 'langSelect-EN').click())
driver.implicitly_wait(200)
time.sleep(4)

while True:
    time.sleep(0.25)
    driver.find_element(By.ID, 'bigCookie').click()
