# coding=utf-8

from selenium import webdriver
import os
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
browser = webdriver.Chrome()
browser.implicitly_wait(30)
browser.get("http://h5.m.91nuanyou.com/view/index/index.html")
time.sleep(5)
browser.find_element_by_xpath('//*[@id="my"]/span').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input').send_keys('13771775285')
time.sleep(5)
browser.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[2]/div[2]/input').send_keys('kim_zheng')
time.sleep(5)
browser.find_element_by_xpath('/html/body/div/div/div/div[3]/form/button').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="my"]/span').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/span[1]').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/p[3]/span[2]').click()
time.sleep(10)
test= browser.find_elements_by_xpath('//*[@id="main"]/div[3]/div[1]/div[2]/input')
test.send_keys('C:\\WORK\\workspace\\open.jpg')
# print browser.title
# os.system("pause")
browser.quit()
