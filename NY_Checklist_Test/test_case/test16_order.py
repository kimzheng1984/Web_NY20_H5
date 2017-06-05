# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""我的订单"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input').send_keys('13771775285')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[2]/div[2]/input').send_keys('kim_zheng')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/button').click()
        time.sleep(3)

    # 我的订单
    def test16_order(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="orderListView"]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\order.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/div[4]').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\order1.jpg")
        time.sleep(2)
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
