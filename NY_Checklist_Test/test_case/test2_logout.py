# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""登出"""
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

    # case2: 登出
    def test2_logout(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        try:
            self.assertEqual(u'我的', driver.title)
        except AssertionError:
            print u'我的页面异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\logout1.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'我的信息', driver.title)
        except AssertionError:
            print u'我的信息异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\logout2.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div[3]/div[4]/button').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\logout3.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="confirm-h5"]/div/div[3]/div[2]').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'返回首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\logout4.jpg")
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
