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
search.send_keys('Python Developer')
search.send_keys(Keys.ENTER)

options = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Show all filters. Clicking this button displays all available filter options."]')))
options.click()

entry = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'label[for="advanced-filter-experience-2"]')))
entry.click()

time.sleep(1)

remote = driver.find_element(By.CSS_SELECTOR, 'label[for="advanced-filter-workplaceType-2"]')
remote.click()

time.sleep(1)

search = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Apply current filters to show results"]')
search.click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".reusable-search__filters-bar-selected-filters-reset")))
items = driver.find_elements(By.CSS_SELECTOR, '#main > div > div.scaffold-layout__list > div > ul li')

for item in items:
    
    item.click()
    time.sleep(2)
    save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.jobs-details__main-content .jobs-save-button')))
    save.click()
    time.sleep(2)

driver.quit()