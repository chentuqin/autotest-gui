#coding = utf-8
import unittest,os,sys,time
import logging,logging.config
base_dir = os.path.dirname(os.path.abspath(__file__))
base = base_dir.split('\src')[0]
case_dir = base+"\\src\\case\\hpcase"
sys.path.append(base+'\src')
base1 = os.path.abspath(os.path.dirname(base) + os.path.sep + ".")
from common import HTMLTestRunner


logging.config.fileConfig(base+"\\config\\hp.conf")

def testSuite():
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_dir,pattern = 'test_*.py',top_level_dir=None)
	for suit in discover:
		for case in suit:
			testunit.addTests(case)
	logging.info(testunit)
	return testunit

'''start_dir：要测试的模块名或测试用例目录

pattern='test*.py'：表示用例文件名的匹配原则。此处匹配以“test”开头的.py 类型的文件，* 表示任意多个字符

top_level_dir= None 测试模块的顶层目录，如果没有顶层目录，默认为None'''


if __name__ == "__main__":

	nowtime = time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))
	filename = base + "\\report\\report\\" + "test_all_hp_" + nowtime + ".html"
	fp = open(filename,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'机票预定自动化测试报告',description=u'测试用例执行结果')
	runner.run(testSuite())
	fp.close()