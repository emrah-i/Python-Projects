from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

count = driver.find_element(value='articlecount')
print('Total wikipedia article count is:', count.text.split(" ")[0])

driver.quit()