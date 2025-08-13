import time

from selenium import webdriver



viewports = [(1024,768), (768,1024),(375,667),(414,896)]
driver = webdriver.Firefox()
driver.get('https://www.google.com/')

# driver.set_window_size(768,1024)  #this will set the windows size according to the provided height and width

try:
    for width,height in viewports:
        driver.set_window_size(width,height)  # this command change the window size according to the viewport of array we given
        time.sleep(3)
finally:
    driver.close()