# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    u"""评论"""
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

    def test7_comment(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        try:
            self.assertEqual(u'我的', driver.title)
        except AssertionError:
            print u'我的页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\comment.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/span[2]').click()
        try:
            self.assertEqual(u'我的订单', driver.title)
        except AssertionError:
            print u'我的订单页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\comment1.jpg")
        time.sleep(3)
        driver.find_element_by_css_selector('#main > div > div > div > div.order-content-list.candelete.ng-scope > div > div.swiper-wrapper > div.swiper-slide.show-box.swiper-slide-active > div > div.boxflex.show-txt > div > p.status > span.button-nail.ng-binding.button-nail-red').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/span').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\comment2.jpg")
        time.sleep(3)
        driver.find_element_by_css_selector('#content').send_keys(u'真方便快捷，下次还会光顾，暖游真给力，值得推荐！')
        time.sleep(5)
        driver.find_element_by_css_selector('#main > div.comment-score > div.score-box > div:nth-child(5)').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\selenium\\NY_Checklist_Test\\report\\comment3.jpg")
        time.sleep(5)
        driver.find_element_by_css_selector('#main > div.pay-button > span').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()