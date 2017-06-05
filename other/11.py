# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time

class NY(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

    def test1(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.quit()

    def test2(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/span').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()