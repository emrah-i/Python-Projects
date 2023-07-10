from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

wait = WebDriverWait(driver, 10)

email = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
email.send_keys('emrakhibragimov5@gmail.com')
sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys('Acdc1234!')
sleep(1)
submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit.click()

sleep(5)

driver.get('https://www.instagram.com/chefsteps/')

followers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header > section > ul > li:nth-child(2) a')))
followers.click()

sleep(3)

for i in range(50):
    follow = driver.find_element(By.CSS_SELECTOR, f'div[role="dialog"] > div > div > div > div > div > div > div > div:nth-child({i+1}) > div > div > div > div > div > button')
    follow.click()
    sleep(1.5)

sleep(5)

driver.quit()
