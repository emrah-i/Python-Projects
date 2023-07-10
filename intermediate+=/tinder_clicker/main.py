from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://tinder.com/')

wait = WebDriverWait(driver, 10)

si = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-size="medium"]')))
si.click()

google = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="button"]')))
google.click()

wait.until(EC.number_of_windows_to_be(2))
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
email.send_keys("emrakhibragimov5@gmail.com")
email.send_keys(Keys.ENTER)

password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
password.send_keys("Acdc1234!")
password.send_keys(Keys.ENTER)

time.sleep(10)

og_window = driver.window_handles[0]
driver.switch_to.window(og_window)

allow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Allow"]')))
allow.click()

nt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Not interested"]')))
nt.click()

everything = driver.find_element(By.CSS_SELECTOR, 'main')
action_chains = ActionChains(driver)

for _ in range(100):
    time.sleep(5)
    action_chains.move_to_element(everything).send_keys(Keys.ARROW_LEFT).perform()                          

time.sleep(1000)

driver.quit()