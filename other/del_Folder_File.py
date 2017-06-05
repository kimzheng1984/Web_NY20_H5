# -- coding: UTF-8

import os
import shutil

delList = []
delDir = '/WORK/workspace/python/selenium/NY_Checklist_Test/report/'
delList = os.listdir(delDir)

for f in delList:
    filePath = os.path.join(delDir, f)
    if os.path.isfile(filePath):
        os.remove(filePath)
        # print filePath + 'was removed!'
    elif os.path.isdir(filePath):
        shutil.rmtree(filePath, True)
        # print "Directory:" + filePath + "was removed!"
