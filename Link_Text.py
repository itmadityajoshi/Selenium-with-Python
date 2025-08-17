

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/v1/')
driver.maximize_window()
time.sleep(3)

#Login into the site
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#login-button').click()


#finding elements or title by using LINk_TEXT
driver.find_element(By.LINK_TEXT, 'Sauce Labs Backpack').click()  #it will find the link text element and perform the click operations
time.sleep(5)