# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""更多攻略"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    # 更多攻略
    def test9_guide(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]').click()
        time.sleep(5)
        try:
            self.assertEqual(u'实用攻略', driver.title)
        except AssertionError:
            print u'实用攻略异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\NY_Checklist_Test\\report\\guide.jpg")
        time.sleep(3)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
