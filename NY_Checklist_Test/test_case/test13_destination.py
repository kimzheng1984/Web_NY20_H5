# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""目的地"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    # 目的地
    def test13_destination(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        time.sleep(3)
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\d.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\korea.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        time.sleep(3)
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\jap.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[3]').click()
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\tha.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\ge.jpg")
        time.sleep(3)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
