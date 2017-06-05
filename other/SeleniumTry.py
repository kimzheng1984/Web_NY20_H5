# -- coding: UTF-8 --
from selenium import webdriver
import os
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
driver = webdriver.Chrome()
# try:
driver.get("http://www.baidu.com")
# except Exception, e:
#     print Exception,":", e
# # time.sleep(300)

driver.find_element_by_id("kw").send_keys(u'郑国志')
driver.find_element_by_id("su").click()
os.system("pause")
driver.quit()