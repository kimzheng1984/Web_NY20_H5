# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""周边"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    # 周边
    def test10_nearby(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/span').click()
        time.sleep(2)
        try:
            self.assertEqual(u'地图搜索', driver.title)
        except AssertionError:
            print u'地图搜索异常'
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\nearby.jpg")
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
