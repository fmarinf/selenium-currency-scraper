from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

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

def parse_currency(currency):
  country_origin = currency.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[1]')
  origin_currency = country_origin.text
  
  clp_equiv = currency.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[2]/a')
  clp_equivalent = float(clp_equiv.text)
  
  conv_url = clp_equiv.get_attribute('href')

  clp_inv = currency.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[3]/a')
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
  currency_data = [parse_currency(currency) for currency in currencies[:10]]
  print(currency_data)
 
  print('Saving as CSV..')
  currencies_df = pd.DataFrame(currency_data)
  print(currencies_df)
  currencies_df.to_csv('currencies.csv', index=None)