#coding=utf-8
from selenium import webdriver
import unittest,os,sys,time,logging,xlrd,re
import logging

base_dir = os.path.dirname(os.path.dirname(__file__))
base = base_dir.split('\case')[0]
sys.path.append(base+'\page')
sys.path.append(base+'\case')
sys.path.append(base)

base1 = base_dir.split('\src')[0]
sys.path.append(base+'\src')
data = xlrd.open_workbook(base1+'\\data\\hp.xlsx')

#获取网址
test_url = data.sheet_by_name("url")
url = test_url.row_values(1)[0]

#获取用户
hp_login = data.sheet_by_name("账户密码")
username = hp_login.row_values(1)[0]
password = hp_login.row_values(1)[1]

#获取参数
parameter = data.sheet_by_name("订票参数")
passengers_number = parameter.row_values(2)[1]

from common import basepage,login
from page.hppage import planeticket

class HpPlaneFlights(unittest.TestCase):


	def setUp(self):
		logging.info('自动化开始')
		self.driver = webdriver.Chrome(base1+'\\driver\\chromedriver.exe')
		li = login.HpLogin(self.driver)  
		li.open(url)
		time.sleep(1)
		li.hplogin(username,password)
		time.sleep(3)


	def tearDown(self):
		basepage.Action.screenshot(self)  
		logging.info("订票测试结束!")
		logging.info("=========================")
        #获取页面console.log()
		for entry in self.driver.get_log('browser'):
			print("%s",entry)
		self.driver.quit()

	def test_booking_plane(self):
		u'''机票预定开始'''
		print("订票开始")
		bk = planeticket.PlaneTicketPage(self.driver)
		bk.booking_flights()
		print("结束")

		#选择机票
		bk.select_flight()
		'''money1 = re.findall(r'\d+',bk.get_money1())
		print("money1======"+money1)
		money2 = re.findall(r'\d+',bk.get_money2())
		print("money2======"+money2)'''
		#支付机票
		bk.pay_details()

		self.assertEqual(bk.get_thanktest(),"Thank you for booking through Web Tours.")
		#money1 = bk.get_money1()
		#money2 = bk.get_money2()
		#moneys = bk.get_moneys()

	'''	moneys = re.findall(r'\d+',bk.get_moneys())
		print("moneys======"+moneys)

		mon = int(money1)*passengers_number+int(money2)*passengers_number
		self.assertEqual(int(moneys),mon)
'''


if __name__ == "__main__":
	unittest.main()
