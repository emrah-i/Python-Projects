from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(by='name', value='fName')
fname.send_keys('Alf')

lname = driver.find_element(by='name', value='lName')
lname.send_keys('Johnson')

email = driver.find_element(by='name', value='email')
email.send_keys('ahhh@me.com')
email.send_keys(Keys.ENTER)

#button = driver.find_element(by='tag name', value='button')
#button.click()

time.sleep(3)

driver.quit()