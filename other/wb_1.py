#! usr/python/bin
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

# geckodriver = 'C:\Program Files (x86)\Mozilla Firefox'
dr = webdriver.Firefox()
time.sleep(60)

dr.get('http://www.baidu.com')
print "closed"
dr.close()

# from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# #
# # browser = webdriver.Firefox()
# #
# # browser.get('http://www.yahoo.com')
# # assert 'Yahoo!' in browser.title
# #
# # elem = browser.find_element_by_name('p')  # Find the search box
# # elem.send_keys('seleniumhq' + Keys.RETURN)
# #
# # browser.quit()

