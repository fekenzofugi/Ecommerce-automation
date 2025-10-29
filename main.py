import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.mercadolivre.com.br")

# Load saved cookies
for cookie in pickle.load(open("ml_cookies.pkl", "rb")):
    driver.add_cookie(cookie)
driver.refresh()

time.sleep(5)
