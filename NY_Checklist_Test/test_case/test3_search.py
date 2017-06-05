# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""搜索-地图与商户"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    def test3_search(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/a').click()
        try:
            self.assertEqual(u'搜索', driver.title)
        except AssertionError:
            print u'搜索异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search.jpg")
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/input').send_keys(u'炸鸡')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/span[1]').click()
        time.sleep(3)
        try:
            self.assertEqual(u'地图搜索', driver.title)
        except AssertionError:
            print u'地图搜索异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search1.jpg")
        driver.back()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/span/span[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/span[1]').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商户搜索异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search2.jpg")
        driver.find_element_by_xpath('//*[@id="mchList"]/div[2]/div[1]').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家详情', driver.title)
        except AssertionError:
            print u'商家详情页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search3.jpg")
        # driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div[2]/img').click()
        # time.sleep(3)
        # try:
        #     self.assertEqual(u'地图导航', driver.title)
        # except AssertionError:
        #     print u'地图选项异常'
        # time.sleep(2)
        # driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search4.jpg")
        # driver.back()
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="youfu"]/div[2]/div[2]/div[2]/a').click()
        # time.sleep(3)
        # try:
        #     self.assertEqual(u'用户登录', driver.title)
        # except AssertionError:
        #     print u'用户登录页异常'
        # time.sleep(3)
        # driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search5.jpg")
        # driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input').send_keys('13771775285')
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[2]/div[2]/input').send_keys('kim_zheng')
        # time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/button').click()
        # time.sleep(3)
        # try:
        #     self.assertEqual(u'商家详情', driver.title)
        # except AssertionError:
        #     print u'商家详情页异常'
        # time.sleep(3)
        # driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\search6.jpg")
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
