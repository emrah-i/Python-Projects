from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.speedtest.net/')

wait = WebDriverWait(driver, 10)

test = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-label="start speed test - connection type multi"]')))
test.click()

sleep(50)

ds = driver.find_element(By.CSS_SELECTOR, 'div[title="Receiving Time"] .result-data span')
download = ds.text

us = driver.find_element(By.CSS_SELECTOR, 'div[title="Sending Time"] .result-data span')
upload = us.text

driver.get('https://twitter.com/')

name = wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
name.send_keys('Jamal7804097802')
name.send_keys(Keys.ENTER)

password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
password.send_keys('Acdc1234!')
password.send_keys(Keys.ENTER)

text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.public-DraftStyleDefault-block')))
text.click()
text.send_keys(f"My download speed is {download} Mbps and my upload speed is {upload} Mbps.")

sleep(5)

button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]') 
button.click()

sleep(15)
driver.quit()