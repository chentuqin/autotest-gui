#coding=utf-8
import unittest, shutil
import time, os, sys, io
import logging, logging.config
base_dir = os.path.dirname(os.path.abspath(__file__))
base = base_dir.split('\src\suite')[0]
case_dir = base + "\\src\\case\\hpcase"
sys.path.append(base+'\src')
sys.path.append(base)

logging.config.fileConfig(base + "\\config\\hp.conf")
os.path.abspath(os.path.dirname(base) + os.path.sep + ".")
#print(base1+"hhhhhhhhh")
from common import HTMLTestRunner184

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')
#reportname = '产品库自动化测试报告'
reportname = "test_all_hp"

def testSuite():                          
    testunit = unittest.TestSuite()
    #找出所有用例
    discover = unittest.defaultTestLoader.discover(case_dir,    
    pattern = 'test_*.py',                               
    top_level_dir = None)              
    for suite in discover:           
        for case in suite:
            testunit.addTests(case)
    logging.info(testunit)
    return testunit

def rename():
    old_file_name = base + '\\report\\report\\' + reportname + '.html'
    new_file_name = base + '\\report\\report\\' + reportname + '_' + nowtime + "_.html"
    #old_file_name.replace(old_file_name, new_file_name)    
    os.chdir(base)
    os.rename(old_file_name, new_file_name)

'''
def copy_file():
    old_file = filename
    new_file = "F:\\PythonDemo\\autotest-gui\\report\\report\\" + reportname + ".html"
    shutil.copyfile(old_file,new_file)
'''

if __name__ == "__main__":
    nowtime = time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))
    rename()
    filename = base + '\\report\\report\\' + reportname + ".html"   
    fp = open(filename,'wb')
    runner = HTMLTestRunner184.HTMLTestRunner(stream=fp,title='机票预定自动化测试报告',description='测试用例执行结果')
    runner.run(testSuite())   
    fp.close()
    #copy_file()