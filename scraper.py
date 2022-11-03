import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CURRENCY_CLP_URL = 'https://www.x-rates.com/table/?from=CLP&amount=1'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_values(driver):
  CURRENCY_TAG = 'tr'
  driver.get(CURRENCY_CLP_URL)
  currencies = driver.find_elements(By.TAG_NAME,CURRENCY_TAG)
  return currencies

def parse_currency(currency, x):
  country_origin = currency.find_element(By.XPATH,f'//*[@id="content"]//div[1]//div//div[1]//div[1]//table[1]//tbody/tr[{x}]//td[1]')
  origin_currency = country_origin.text
    
  clp_equiv = currency.find_element(By.XPATH,f'//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[{x}]/td[2]/a')
  clp_equivalent = float(clp_equiv.text)
    
  conv_url = clp_equiv.get_attribute('href')
  
  clp_inv = currency.find_element(By.XPATH,f'//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[{x}]/td[3]/a')
  clp_inverted = float(clp_inv.text)

  return {
    'currency': origin_currency,
    'clp_equivalent': clp_equivalent,
    'conversion_url': conv_url,
    'inverted_clp': clp_inverted
    }

if __name__ == "__main__":
  print('Creating driver...')
  driver = get_driver()
  
  print('Fetching currency values...')
  currencies = get_values(driver)
  
  print(f'Found {len(currencies)} values')

  # countryCurr, eqClp, invClp

  print('Parsing top 10 currencies: ')
  currency_data = []
  for currency, x in zip(currencies[:10] , range(1, 11)):
    currency_data.append(parse_currency(currency, x))
    x+=1
    
  # currency_data = [parse_currency(currency) for currency in currencies[:10]]

  jsonStr = json.dumps(currency_data, indent=4)
  print(jsonStr)