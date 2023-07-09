from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.python.org/')

list = driver.find_element(by='xpath', value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
items = list.find_elements(by='xpath', value='./li')

events = {i :{'time': items[i].text[0:10], 'name': items[i].text[10:].replace('\n', '')} for i in range(len(items))}
print(events)

driver.quit()