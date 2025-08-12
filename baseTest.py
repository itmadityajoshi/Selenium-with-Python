from logging import disable

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/v1/') #to og url
driver.implicitly_wait(5)
driver.maximize_window()  # it maximize the windows

driver.find_element(By.ID, 'user-name').send_keys('standard_user')  #web elements username is located by Id and send keys help to send data to be tested
driver.find_element(By.ID, 'password').send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
assert not login_button.get_attribute("disabled")
login_button.click()
print(driver.title)

success = driver.find_element(By.CSS_SELECTOR, '.product_label') # this help to test the result the we are expecting.
assert success.text == 'Products'