# -- coding: UTF-8 --

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # 导入IE解除保护模式

# IE解除保护模式
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

# Baidu类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例
class Baidu(unittest.TestCase):
    # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True

    # test_baidu中放置的就是我们的测试脚本了，这部分我们并不陌生；因为我们执行的脚本就在这里
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        driver.close()

    # is_element_present函数用来查找页面元素是否存在，在这里用处不大，通常删除。因为判断页面元素是否存在一般都加在testcase中。
    def is_element_present(self, how, what):
        try:
            self.driver.find_element_by_id(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    # 对弹窗异常的处理
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException, e: return False
        return True

    # 关闭警告和对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出浏览器等
    def tearDown(self):
        self.driver.quit()
        # 对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息
        self.assertAlmostEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unitest.main()函数用来测试 类中以test开头的测试用例
    unittest.main()
