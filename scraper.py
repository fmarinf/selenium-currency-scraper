from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CURRENCY_CLP_URL = 'https://www.x-rates.com/table/?from=CLP&amount=1'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

driver.get(CURRENCY_CLP_URL)

print('Page title: ', driver.title)