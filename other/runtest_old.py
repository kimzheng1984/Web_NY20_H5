# -- coding: UTF-8 --

import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from NY_Checklist_Test.del_Folder_File import Files_removed


test_dir1 = '/WORK/workspace/python/selenium/NY_Checklist_Test/test_case/'
test_dir2 = '/WORK/workspace/python/selenium/NY_Checklist_Test/report/'
discover = unittest.defaultTestLoader.discover(test_dir1, pattern='test1_login.py')

if __name__ == '__main__':
    Files_removed()
    # 打印log
    # log_file = '/WORK/workspace/python/selenium/NY_Checklist_Test/report/log_file.txt'
    # f = open('log_file.txt', 'w')
    # f = open(log_file, "w")
    # runner = unittest.TextTestRunner(f)
    # runner.run(discover)
    # f.close()

    # 产生HTML测试报告
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = test_dir2 + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'暖游Checklist自动化测试报告',
                            description=u'测试概况：',)
    runner.run(discover)
    fp.close()
