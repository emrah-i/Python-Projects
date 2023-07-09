from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

wait = WebDriverWait(driver, 10)

lang = wait.until(EC.visibility_of_element_located((By.ID, "langSelect-EN")))
lang.click()

cookie = wait.until(EC.visibility_of_element_located((By.ID, "bigCookie")))
while True:
    for _ in range(500):
        cookie.click()
    time.sleep(10)


