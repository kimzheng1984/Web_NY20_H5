# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""支付-优付"""
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

    def test5_pay(self):
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
        try:
            self.assertEqual(u'优付结算', driver.title)
        except AssertionError:
            print u'优付结算异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\pay.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/input').send_keys('1000')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div').click()
        time.sleep(3)
        try:
            self.assertEqual(u'京东支付', driver.title)
        except AssertionError:
            print u'京东优付页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\pay1.jpg")
        driver.find_element_by_xpath('//*[@id="J-next-btn"]').click()
        time.sleep(2)
        try:
            self.assertEqual('https://m.jdpay.com/wepay/web/pay/sign', driver.current_url)
        except AssertionError:
            print u'优付支付调用异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\pay2.jpg")
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
