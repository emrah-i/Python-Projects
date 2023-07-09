from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')

wait = WebDriverWait(driver, 15)

email = wait.until(EC.visibility_of_element_located((By.NAME, 'session_key')))
email.send_keys('emrakhibragimov5@gmail.com')

time.sleep(1)

password = driver.find_element(By.NAME, value='session_password')
password.send_keys('emrakh1234')
password.send_keys(Keys.ENTER)

search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))
search.click()
search.send_keys('Python Developer')
search.send_keys(Keys.ENTER)

jobs = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')))
jobs.click()

'''level = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember1317"]/button')))
level.click()
entry = wait.until(EC.visibility_of_element_located((By.ID, 'ember2220')))
child = entry.find_element(By.XPATH, ".//button")
child.click()

level_search = driver.find_element(By.XPATH, '//*[@id="ember1414"')
level_search.click()'''

easy = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ember2244')))
easy.click()

time.sleep(10)

driver.quit()