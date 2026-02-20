from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--lang=en-US")
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Lenovo-ThinkBook-IRL-21SH000GUS-Computer/dp/B0F83ZRQM7/")
try:
    element = driver.find_element(By.CLASS_NAME, "a-price-whole")
    print("Price:", element.text)
    symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
    print("Symbol:", symbol.text)
except Exception as e:
    print(e)
driver.close()
