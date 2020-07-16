#coding = utf-8
from selenium.webdriver.common.by import By
import time,os,sys
base_dir = os.path.dirname(os.path.dirname(__file__))
base = base_dir.split('\page')[0]
sys.path.append(base)
from common import basepage


class HpLogin(basepage.Action):

	username_loc = (By.NAME,"username")
	password_loc = (By.NAME,"password")
	submit_loc = (By.NAME,"login")
	#frame_body_loc = (By.NAME,"body")
	#12345678901234567890frame_navbar_loc = (By.NAME,"navbar")


	def hplogin(self,username,password):
		self.switch_frame(1)   #多层frame,每一级都从0下标开始算
		#self.switch_to_frame(self.frame_body_loc)
		self.switch_frame(0)
		#self.switch_to_frame(self.frame_navbar_loc)
		self.input_text(self.username_loc,username)
		self.input_text(self.password_loc,password)
		self.click(self.submit_loc)
		self.driver.switch_to_default_content()
		print(11111111111111111)