import time

from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()  # this maximize the window tab
# driver.fullscreen_window() #this will make page to full screen
# driver.minimize_window() #this will minimize the screen.
print(driver.title)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '.oxd-text.oxd-text--p.orangehrm-login-forgot-header').click()
time.sleep(5)
driver.back() # this will move back to the original page from the link
time.sleep(5)
driver.forward() # this will forward again to the link that we have choosen in find_elements
time.sleep(5)
driver.refresh() # this will refresh the pages
driver.close()