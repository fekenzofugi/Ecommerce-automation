import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.mercadolivre.com.br")

# Load saved cookies
for cookie in pickle.load(open("ml_cookies.pkl", "rb")):
    driver.add_cookie(cookie)
driver.refresh()

wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

# === HOVER SOBRE O NOME DO USUÁRIO ===
user_span = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.nav-header-username")))
actions.move_to_element(user_span).perform()
time.sleep(1)  # pequena pausa para o menu aparecer

# === AGORA ESPERA O LINK "ANÚNCIOS" ===
listings_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-id="listings"]')))
listings_link.click()

time.sleep(3)
driver.quit()