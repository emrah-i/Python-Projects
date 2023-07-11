from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests

url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
    }

driver = webdriver.Chrome()
actions = ActionChains(driver)
js_executor = driver.execute_script
wait = WebDriverWait(driver, 10)

driver.get(url)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="grid-search-results"] h1')))
div = driver.find_element(By.CSS_SELECTOR, 'div[id="grid-search-results"] h1')
div.click()
next = driver.find_element(By.CSS_SELECTOR, 'a[title="Next page"]')
html = ''

for _ in range(2):
    for _ in range(300):
        actions.send_keys(Keys.ARROW_DOWN).perform()

    sleep(3)
    html += driver.page_source
    next.click()

sleep(10)

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfAHbmSuAX7Mjg4wYCEl9WI7iwX6h1BkWYxGAbkP2hUBI1F2g/viewform')
sleep(3)

soup = BeautifulSoup(html, "html.parser")
adds = soup.select('#search-page-list-container div ul li div article[role="presentation"] div div a address')
links = soup.select('#search-page-list-container div ul li div article[role="presentation"] div div a')
prices = soup.select('span[data-test="property-card-price"]')
for i in range(len(adds)):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Your answer"]')))
    all = driver.find_elements(By.CSS_SELECTOR, 'textarea[aria-label="Your answer"]')
    address = all[0]
    price = all[1]
    link = all[2]

    address.send_keys(adds[i].text)
    price.send_keys(prices[i].text)
    if links[i]['href'].startswith('/'):
        send = f'https://www.zillow.com{links[i]["href"]}'
        link.send_keys(send)
    else:
        link.send_keys(links[i]['href'])
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' div[role="button"]')))
    buttons = driver.find_elements(By.CSS_SELECTOR, ' div[role="button"]')
    buttons[0].click()
    sleep(2)

    back = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Submit another response')))
    back.click()
    
driver.quit()