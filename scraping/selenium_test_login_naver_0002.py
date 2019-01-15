from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

if os.name == 'nt':
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe')
elif os.name == 'posix':
    driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')
else:
    print("Not supported OS")
    exit()

url = "https://www.naver.com/"

driver.get(url)
driver.implicitly_wait(10)

driver.find_element_by_class_name('lg_local_btn').click()
driver.implicitly_wait(7)

id_tag = driver.find_element_by_id('id')
pw_tag = driver.find_element_by_id('pw')
actions = ActionChains(driver)
actions.pause(2)

driver.execute_script( "document.getElementById('id').value = 'jskd2938'" )
driver.implicitly_wait(5)
id_tag.send_keys(Keys.TAB)
actions.pause(2)

driver.execute_script( "document.getElementById('pw').value = 'ahsgjs&3g'")
driver.implicitly_wait(5)
driver.find_element_by_class_name('btn_global').click()

