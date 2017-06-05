# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""商圈"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    def test4_district(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换日本
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[2]').click()
        time.sleep(2)
        # 银座商圈
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district1.jpg")
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district2.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换泰国
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[3]').click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district3.jpg")
        time.sleep(2)
        # 曼谷商圈
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district4.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换德国
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[4]').click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district5.jpg")
        time.sleep(2)
        # 柏林商圈
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\district6.jpg")
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
