#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


import time,os,sys
base_dir = os.path.dirname(os.path.dirname(__file__))
base = base_dir.split('\page')[0]
sys.path.append(base)
from common import basepage

class BaiDuPage(basepage.Action):

	baidu_sousuok_loc = (By.ID,"kw")
	baidu_submit_loc = (By.ID,"su")
	baidu_list_loc = (By.LINK_TEXT,"多语种即时在线翻译_百度翻译")
	baidu_fanyishuru_loc = (By.ID,"baidu_translate_input")
	baidu_results_loc = (By.CLASS_NAME,"ordinary-span-edit")

	def sousuo(self,souName):
		self.input_text(self.baidu_sousuok_loc,souName)
		self.click(self.baidu_submit_loc)
		self.click(self.baidu_list_loc)
		js="document.getElementById('baidu_translate_input').value='cat'"
		ss.driver.execute_script(js)
		self.keys_space(self.baidu_fanyishuru_loc)
		time.sleep(2)

	def get_results(self):
		return self.get_text(self.baidu_results_loc)
		