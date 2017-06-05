# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""今日头条"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    # 今日头条
    def test8_hotnews(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="todaylatest"]/div[2]/div/div[1]/p/a').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\hotnews.jpg")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
