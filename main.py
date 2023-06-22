import csv
import random

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.set_window_size(1700, 800)
time.sleep(1)

browser.get('https://labsafe.nwafu.edu.cn/index.php')

click_login = browser.find_element(By.CSS_SELECTOR, '.loginForm > div > a').click()

browser.find_element(By.ID, 'username').send_keys('2022060629')
browser.find_element(By.ID, 'password').send_keys('Yangyang123')
browser.find_element(By.ID, 'login_submit').click()
time.sleep(1)

move = browser.find_element(By.XPATH, '//*[@id="cg_nav_onea"][3]/a')

time.sleep(1)
ActionChains(browser).move_to_element(move).perform()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="cg_nav_onea"][3]/ul/li[1]/a').click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.module-right > .zxxxy > ul > li > a').click()

for i in range(382):
    time.sleep(60*6)
    browser.switch_to.alert.accept()
    print(i, "  ", i * 5)

