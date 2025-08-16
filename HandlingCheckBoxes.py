from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='gender']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[7]//div[1]//div[1]//div[2]//input[1]").click()
time.sleep(3)
driver.quit()

