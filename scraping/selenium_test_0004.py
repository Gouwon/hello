import time
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")    # or.   options.add_argument("--disable-gpu")
# UserAgent값을 바꿔줍시다!

if os.name == "nt":
    options.add_argument("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe', options=options)
    # driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)
elif os.name == "posix":
    driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')


driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("./results/images/bbb.png")   # or.  driver.get_screenshot_as_file('bbb.png')
driver.implicitly_wait(5)
driver.quit()