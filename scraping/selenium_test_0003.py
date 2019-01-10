import time
from selenium import webdriver

## NOT RECOMMEND

driver = webdriver.PhantomJS()
driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("./results/images/aaa.png")
driver.implicitly_wait(5)
driver.quit()

# But, …
# Selenium support for PhantomJS has been deprecated!! (from 2017)
# Please use headless versions of Chrome or Firefox instead