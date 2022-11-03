# selenium-currency-scraper
Scrape different currencies using Selenium and AWS Lambda.

The lambda function required two layers:

- Used pipenv to create a virtual environment locally (download from: https://www.python.org/downloads/release/python-374/).
- Selenium installation and simulation of original python directory for required zip:
``` bash
pip install selenium==3.8.0 -t python/lib/python3.7/site-packages
```
- Chromedriver installation
``` bash
mkdir -p chromedriver
cd chromedriver
curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
```
- Chrome binary
``` bash
curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-41/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
```

** Compress both files (Chromedriver + Chrome binary) in chromedriver.zip **

- Test the 2 layers setup using:
``` bash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    driver.get('https://www.google.com/')

    driver.close();
    driver.quit();

    response = {
        "statusCode": 200,
        "body": "Selenium Headless Chrome Initialized"
    }

    return response
    ```

