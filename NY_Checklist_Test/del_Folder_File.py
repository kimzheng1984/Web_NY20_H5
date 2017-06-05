# -- coding: UTF-8

import os
import shutil

# 删除report文件下的log、截图与测试报告
class Files_removed():
    delList = []
    delDir = '/WORK/workspace/python/selenium/NY_Checklist_Test/report/'
    def __init__(self):
        self.delList = os.listdir(self.delDir)
        for f in self.delList:
            self.filePath = os.path.join(self.delDir, f)
            if os.path.isfile(self.filePath):
                os.remove(self.filePath)
                # print self.filePath + 'was removed!'
            elif os.path.isdir(self.filePath):
                shutil.rmtree(self.filePath, True)
                # print "Directory:" + self.filePath + "was removed!"
