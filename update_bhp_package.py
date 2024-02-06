from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# handle selenium close automatic after test run
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://marcksvenus-clinic.buaya.dev/")

# LOGIN
driver.find_element(By.ID, 'username').send_keys("adminss")
driver.find_element(By.ID, 'password').send_keys("123456")
driver.find_element(By.ID, 'btnppLogin').click()

# Hoverable Layanan
driver.implicitly_wait(5)
hoverable = driver.find_element(By.PARTIAL_LINK_TEXT, "Master")
ActionChains(driver).move_to_element(hoverable).perform()

# Hoverable Promo
driver.implicitly_wait(5)
hoverable = driver.find_element(By.PARTIAL_LINK_TEXT, "Master Layanan")
ActionChains(driver).move_to_element(hoverable).perform()

# Master Promo Click
driver.find_element(By.PARTIAL_LINK_TEXT, "Treatment Paket").click()

workbook = load_workbook('C:\\Users\\BVK PC\\Desktop\\Marvee\\master-bhp.xlsx')

sheet = workbook['Sheet3']

# =====================================================================================================#
cari_nama = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
cari_nama.send_keys("IMMUNE BOOSTER INJECTION (6X)")
time.sleep(1)

kode_item = driver.find_element(By.PARTIAL_LINK_TEXT, "IMMUNE BOOSTER INJECTION (6X)")
kode_item.click()
# =====================================================================================================#

i = 2
while i <= len(sheet['C']):
    input_bhp = sheet['C' + str(i)].value
    total_bhp = sheet['D' + str(i)].value

    time.sleep(1)
    add_bhp = driver.find_element(By.CSS_SELECTOR, '.btnTambahbhp')
    add_bhp.click()

    driver.implicitly_wait(10)
    tambah_bhp = driver.find_element(By.CSS_SELECTOR, '.select2-selection__arrow')
    tambah_bhp.click()
    
    cari_bhp = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
    cari_bhp.send_keys(input_bhp)
    cari_bhp.send_keys(Keys.ENTER)

    jumlah_bhp = driver.find_element(By.NAME, 'jumlah')
    jumlah_bhp.send_keys(total_bhp)

    simpan = driver.find_element(By.XPATH, '//*[@id="form-modal"]/form/div/div/div[3]/button[1]')
    simpan.click()

    time.sleep(1)

    i += 1