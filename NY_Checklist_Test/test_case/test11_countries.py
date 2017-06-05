# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""不同国家切换"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    # 不同国家切换
    def test10_nearby(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country2').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\jap.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country3').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\tha.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country4').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\germany.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country1').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\korea.jpg")
        time.sleep(3)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
