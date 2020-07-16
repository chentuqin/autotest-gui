#coding=utf-8
from selenium import webdriver
import unittest,os,sys,time,logging,xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

base_dir = os.path.dirname(os.path.dirname(__file__))
base = base_dir.split("\case")[0]
print(base+"eeeee")
sys.path.append(base+"\page")
sys.path.append(base+"\case")
sys.path.append(base)
from baidupage import baidusou
from common import basepage
import logging,logging.config

base1 = base_dir.split("\src")[0]
sys.path.append(base1+"\data")
sys.path.append(base1)
print(base1+"====")
data = xlrd.open_workbook(base1+"\\data\\baidusousuo.xlsx")

baidu_url = data.sheet_by_name("百度搜索")
url = baidu_url.row_values(1)[1]

#获取页面cosole.log()配置
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {'browser':'ALL'}

class BaiDuSou(unittest.TestCase):

	def setUp(self):
		logging.info("百度搜索自动化测试开始")
		self.driver = webdriver.Chrome(base1 + "\driver\chromedriver.exe")
		ll = baidusou.BaiDuPage(self.driver)
		ll.open('https://fanyi.baidu.com/translate')
		time.sleep(1)

	def tearDown(self):
		basepage.Action.screenshot(self)
		logging.info("百度搜索测试结束")
		for entry in self.driver.get_log('browser'):
			print("%s",entry)
		self.driver.quit()


	def test_baiduSou(self):
		ss = baidusou.BaiDuPage(self.driver)
		souName = '百度翻译'
		ss.sousuo()

		self.assertEqual(ss.get_results(),"猫")
		logging.info("翻译成功")


if __name__ == '__main__':
	unittest.main()