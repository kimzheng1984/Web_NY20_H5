# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""优惠劵"""
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

    def test6_coupon(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[2]/span[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[2]/div/a[3]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="mchList"]/div[2]/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="youfu"]/div[2]/div[2]/div[2]/a').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="coupon"]/div[2]/div').click()
        time.sleep(3)
        try:
            self.assertEqual(u'选择优惠劵', driver.title)
        except AssertionError:
            print u'选择优惠劵页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\coupon.jpg")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        try:
            self.assertEqual(u'优付结算', driver.title)
        except AssertionError:
            print u'优付结算页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\coupon1.jpg")
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
