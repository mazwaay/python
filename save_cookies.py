from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pickle
import os

option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox")        
driver = webdriver.Chrome(options=option)
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fmaps%2F%40-2.44565%2C117.8888%2C4z%3Fentry%3Dttu&ec=GAZAcQ&hl=id&ifkv=ASKXGp1_MDLIO33iR9mK6gGPPCy7yZlo4gWzTCBm3JlsY_D9Mwp5TCeLPvMggCJZK9BsHRH-HPbS4Q&passive=true&service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1409467642%3A1707207965927408&theme=glif")
time.sleep(5)
if os.path.exists('cookies.pkl'):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

print(cookie)

