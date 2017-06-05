# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""开启与登录"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"

    # case1: 开启/登录
    def test1_login(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\login1.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\login2.jpg")
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input').send_keys('13771775285')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[2]/div[2]/input').send_keys('kim_zheng')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/button').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'返回首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\login3.jpg")
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
