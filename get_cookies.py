import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.mercadolivre.com.br")

print("Faça login manualmente. Quando terminar, pressione Enter aqui...")
input()

pickle.dump(driver.get_cookies(), open("ml_cookies.pkl", "wb"))
driver.quit()