import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform

os = platform.system()

if os == "Windows":
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe')
    ctrl = Keys.CONTROL
elif os == "Darwin": 
    driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')  # mac or linux
    ctrl = Keys.COMMAND
else:
    print("Not supported OS")
    exit()

driver.get("https://www.google.com")
time.sleep(2)

inputElement = driver.find_element_by_name("q")
inputElement.send_keys("세종대왕")
inputElement.send_keys(ctrl, 'a')
inputElement.send_keys(ctrl, 'v')
inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()
