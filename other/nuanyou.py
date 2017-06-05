# -- coding: UTF-8 --

from selenium import webdriver
import unittest
import time


class NY(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://h5.m.91nuanyou.com/view/index/index.html"

    # case1: 开启/登录/退出
    def test1_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case1\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case1\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case1\\home.jpg")
        driver.close()

    # case2: 搜索
    def test2_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\open.jpg")
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/a').click()
        try:
            self.assertEqual(u'搜索', driver.title)
        except AssertionError:
            print u'搜索异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\search.jpg")
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/input').send_keys(u'炸鸡')
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/span[1]').click()
        time.sleep(3)
        try:
            self.assertEqual(u'地图搜索', driver.title)
        except AssertionError:
            print u'地图搜索异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\map.jpg")
        driver.back()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/span/span[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[2]/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div/form/div/div[3]/span[1]').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商户搜索异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\list.jpg")
        driver.find_element_by_xpath('//*[@id="mchList"]/div[2]/div[1]').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家详情', driver.title)
        except AssertionError:
            print u'商家详情页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\detail.jpg")
        driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div[2]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'地图导航', driver.title)
        except AssertionError:
            print u'地图选项异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\map1.jpg")
        driver.back()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="youfu"]/div[2]/div[2]/div[2]/a').click()
        time.sleep(3)
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\login.jpg")
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[1]/div[2]/input').send_keys('13771775285')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/div[2]/div[2]/input').send_keys('kim_zheng')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/div/div[3]/form/button').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家详情', driver.title)
        except AssertionError:
            print u'商家详情页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\detail1.jpg")
        driver.find_element_by_xpath('//*[@id="youfu"]/div[2]/div[2]/div[2]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/input').send_keys('1000')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div').click()
        time.sleep(3)
        try:
            self.assertEqual(u'京东支付', driver.title)
        except AssertionError:
            print u'京东优付页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\pay.jpg")
        driver.find_element_by_xpath('//*[@id="J-next-btn"]').click()
        time.sleep(2)
        try:
            self.assertEqual('https://m.jdpay.com/wepay/web/pay/sign', driver.current_url)
        except AssertionError:
            print u'优付支付调用异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case2\\pay1.jpg")
        # os.system('pause')
        driver.close()

    # case3: 商圈
    def test3_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\open.jpg")
        # 明洞商圈
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\list.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换日本
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[2]').click()
        time.sleep(2)
        # 银座商圈
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\jap.jpg")
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\jap_list.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换泰国
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[3]').click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\tha.jpg")
        time.sleep(2)
        # 曼谷商圈
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\tha_list.jpg")
        time.sleep(2)
        driver.back()
        time.sleep(3)
        # 切换德国
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[2]/div[4]').click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\ge.jpg")
        time.sleep(2)
        # 柏林商圈
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case3\\ge_list.jpg")
        time.sleep(2)
        driver.close()

    # case4: 优惠劵
    def test4_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\open.jpg")
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家页面异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\list.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[2]/span[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div[2]/div/a[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mchList"]/div[2]/div[1]').click()
        time.sleep(2)
        try:
            self.assertEqual(u'商家详情', driver.title)
        except AssertionError:
            print u'商家详情异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\merchant.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="youfu"]/div[2]/div[2]/div[2]/a').click()
        time.sleep(2)
        try:
            self.assertEqual(u'优付结算', driver.title)
        except AssertionError:
            print u'优付结算页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\youfu.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="coupon"]/div[2]/div').click()
        time.sleep(5)
        try:
            self.assertEqual(u'选择优惠劵', driver.title)
        except AssertionError:
            print u'选择优惠劵页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case4\\coupon.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]').click()
        time.sleep(2)
        try:
            self.assertEqual(u'优付结算', driver.title)
        except AssertionError:
            print u'优付结算页异常'
        time.sleep(2)
        driver.close()

    # case5: 评论
    def test5_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case5\\open.jpg")
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case5\\login.jpg")
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
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        try:
            self.assertEqual(u'我的', driver.title)
        except AssertionError:
            print u'我的页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case5\\me.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/span[1]').click()
        try:
            self.assertEqual(u'我的订单', driver.title)
        except AssertionError:
            print u'我的订单页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case5\\comment.jpg")
        time.sleep(5)
        driver.find_element_by_css_selector('#main > div > div > div > div.order-content-list.candelete.ng-scope > div > div.swiper-wrapper > div.swiper-slide.show-box.swiper-slide-active > div > div.boxflex.show-txt > div > p.status > span.button-nail.ng-binding.button-nail-red').click()
        time.sleep(5)
        driver.find_element_by_css_selector('#content').send_keys(u'真方便快捷，下次还会光顾，暖游真给力，值得推荐！')
        time.sleep(5)
        driver.find_element_by_css_selector('#main > div.comment-score > div.score-box > div:nth-child(5)').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case5\\comment1.jpg")
        time.sleep(5)
        driver.find_element_by_css_selector('#main > div.pay-button > span').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        driver.close()

    # case6: 导航
    def test6_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case6\\open.jpg")
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/a[1]/img').click()
        time.sleep(3)
        try:
            self.assertEqual(u'商家列表', driver.title)
        except AssertionError:
            print u'商家列表异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case6\\merchant.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="mchList"]/div[2]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div[2]/img').click()
        time.sleep(2)
        try:
            self.assertEqual(u'地图导航', driver.title)
        except AssertionError:
            print u'地图导航异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case6\\navi.jpg")
        time.sleep(2)
        driver.close()

    # case7: 今日头条
    def test7_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case7\\open.jpg")
        driver.find_element_by_xpath('//*[@id="todaylatest"]/div[2]/div/div[1]/p/a').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case7\\today.jpg")
        time.sleep(3)
        driver.back()
        time.sleep(2)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        driver.close()

    # case8: 更多攻略
    def test8_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case8\\open.jpg")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]').click()
        time.sleep(5)
        try:
            self.assertEqual(u'实用攻略', driver.title)
        except AssertionError:
            print u'实用攻略异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case8\\guide.jpg")
        time.sleep(3)
        driver.close()

    # case9: 周边商家
    def test9_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case9\\open.jpg")
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[1]').click()
        time.sleep(2)
        try:
            self.assertEqual(u'地图搜索', driver.title)
        except AssertionError:
            print u'地图搜索异常'
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case9\\map.jpg")
        time.sleep(3)
        driver.back()
        time.sleep(2)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        driver.close()

    # case10: 不同国家切换
    def test10_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case10\\open.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country2').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case10\\jap.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country3').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case10\\tha.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country4').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case10\\gamery.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="choice-country"]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_class_name('country1').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case10\\korea.jpg")
        time.sleep(3)
        driver.close()

    # case11: 周边
    def test11_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case11\\open.jpg")
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/span').click()
        time.sleep(2)
        try:
            self.assertEqual(u'地图搜索', driver.title)
        except AssertionError:
            print u'地图搜索异常'
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case11\\map.jpg")
        time.sleep(2)
        driver.close()

    # case12: 目的地
    def test12_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\open.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        time.sleep(5)
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\destination.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/img').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\korea.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        time.sleep(5)
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/img').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\jap.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[3]').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\tha.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[3]/span').click()
        try:
            self.assertEqual(u'目的地', driver.title)
        except AssertionError:
            print u'目的地异常'
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/img').click()
        time.sleep(5)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case12\\ge.jpg")
        time.sleep(5)
        driver.close()

    # case13: 客服
    def test13_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case13\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case13\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case13\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[2]/span').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case13\\kefu.jpg")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="easemobWidgetSend"]/textarea').send_keys(u'测试')
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="easemobWidgetSendBtn"]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case13\\kefu1.jpg")
        time.sleep(3)
        driver.quit()

    # case14: 优惠劵
    def test14_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case14\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case14\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case14\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/span[1]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case14\\valid.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/div[2]').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case14\\novalid.jpg")
        time.sleep(2)
        driver.quit()

    # case15: 我的订单
    def test15_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case15\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case15\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case15\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="orderListView"]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case15\\order.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/div[4]').click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case15\\order1.jpg")
        time.sleep(2)
        driver.quit()

    # case16: 实用攻略
    def test16_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case16\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case16\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case16\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case16\\guide.jpg")
        time.sleep(2)
        driver.quit()

    # case17: 我的消息
    def test17_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case17\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case17\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case17\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[3]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case17\\message.jpg")
        time.sleep(2)
        driver.quit()

    # case18: 暖游介绍
    def test18_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case18\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case18\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case18\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[4]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case18\\intro.jpg")
        time.sleep(2)
        driver.quit()

    # case19: 旅行赚钱
    def test19_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case19\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case19\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case19\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[5]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case19\\mon.jpg")
        time.sleep(2)
        driver.quit()

    # case20: 我的评论
    def test20_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case20\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case20\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case20\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[6]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case20\\comm.jpg")
        time.sleep(2)
        driver.quit()

    # case21: 我的收藏
    def test21_NY(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'首页', driver.title)
        except AssertionError:
            print u'首页异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case21\\open.jpg")
        # print driver.current_url
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        # print driver.title
        try:
            self.assertEqual(u'用户登录', driver.title)
        except AssertionError:
            print u'用户登录异常'
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case21\\login.jpg")
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
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case21\\home.jpg")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="my"]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[7]/div[2]').click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\selenium\\ny_cases\\case21\\favorate.jpg")
        time.sleep(2)
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
