#coding
from selenium.webdriver.common.by import By
from selenium import webdriver
import time,os,sys,xlrd
import webbrowser

base_dir = os.path.dirname(os.path.dirname(__file__))
base = base_dir.split("\page")[0]
sys.path.append(base)

base1=base_dir.split("\src")[0]
data = xlrd.open_workbook(base1+"\data\hp.xlsx")
parameter = data.sheet_by_name("订票参数")
departure_date = parameter.row_values(0)[1]
arrival_date = parameter.row_values(1)[1]
passengers_number = parameter.row_values(2)[1]
credit_card = parameter.row_values(3)[1]
exp_date = parameter.row_values(4)[1]



from common import basepage

class PlaneTicketPage(basepage.Action):

	flights_loc = (By.XPATH,"/html/body/center/center/a[1]/img")
	#flights_loc = (By.CSS_SELECTOR,"//img[alt='Search Flights Button']")

	#起飞下拉列表
	departure_city_loc = (By.NAME,"depart")
	departure_city_click_loc = (By.XPATH,"//option[contains(text(),'London')]")

	#回程下拉列表
	arrival_city_loc = (By.NAME,"arrive")
	arrival_city_click_loc = (By.XPATH,"//option[contains(text(),'Los Angeles')]")

	#起飞时间
	departure_date_loc = (By.NAME,"departDate")
	#回程时间
	arrival_date_loc = (By.NAME,"returnDate")
	#乘客人数
	passengers_number_loc = (By.NAME,"numPassengers")
	roundtrip_ticket_loc = (By.NAME,"roundtrip")

	seating_Preference_loc = (By.XPATH,"//label[contains(text(),'Window')]")
	type_of_seat_loc = (By.XPATH,"//label[contains(text(),'Business')]")

	#提交
	continue_loc = (By.NAME,"findFlights")

	#选择机票
	select_flight_loc = (By.XPATH,"/html/body/blockquote/form/center/table[1]/tbody/tr[3]/td[1]/input")
	select_flight2_loc = (By.XPATH,"/html/body/blockquote/form/center/table[2]/tbody/tr[3]/td[1]/input")

	#获取机票金额
	get_money1_loc = (By.XPATH,"/html/body/blockquote/form/center/table[1]/tbody/tr[3]/td[3]")
	get_money2_loc = (By.XPATH,"/html/body/blockquote/form/center/table[2]/tbody/tr[3]/td[3]")
	get_moneys_loc = (By.XPATH,"/html/body/blockquote/form/table/tbody/tr[7]/td")

	continue_reserveFlights_loc = (By.NAME,"reserveFlights")

	#信用卡
	credit_card_loc = (By.NAME,"creditCard")
	exp_date_loc = (By.NAME,"expDate")
	continue_buyFlights_loc = (By.NAME,"buyFlights")


	get_thank_test = (By.XPATH,"/html/body/blockquote/center/small/b")

	#提交机票预定信息
	def booking_flights(self):
		self.switch_to_frame(1)
		self.switch_to_frame(0)
		print("====flights_loc")
		try:
			self.click(self.flights_loc)
		except:
			time.sleep(1)
			url = 'http://127.0.0.1:1080/cgi-bin/welcome.pl?page=search'
			webbrowser.open_new_tab(url)

		print("flights_loc")
		self.driver.switch_to_default_content()
		time.sleep(1)
		self.switch_frame(1)
		self.switch_frame(1)
		self.click(self.arrival_city_loc)
		self.click(self.arrival_city_click_loc)
		time.sleep(2)
		self.input_text(self.departure_date_loc,departure_date)
		self.click(self.departure_city_loc)
		time.sleep(1)
		self.click(self.departure_city_click_loc)
		time.sleep(2)
		self.input_text(self.arrival_date_loc,arrival_date)
		self.input_text(self.passengers_number_loc,str(passengers_number))
		self.click(self.roundtrip_ticket_loc)
		self.click(self.seating_Preference_loc)
		self.click(self.type_of_seat_loc)
		self.click(self.continue_loc)

	#获取启程机票金额	
	def get_money1(self):
		return self.get_text(self.get_money1_loc)

	#获取返程机票金额
	def get_money2(self):
		return self.get_text(self.get_money2_loc)

	#获取预定机票总金额
	def get_moneys(self):
		return self.get_text(self.get_moneys_loc)

	def get_thanktest(self):
		return self.get_text(self.get_thank_test)
		
	#选择机票
	def select_flight(self):
		#self.switch_frame(1)
		#self.switch_frame(1)
		self.click(self.select_flight_loc)
		self.click(self.continue_reserveFlights_loc)

	#机票支付
	def pay_details(self):
		time.sleep(1)
		self.input_text(self.credit_card_loc,credit_card)
		time.sleep(1)
		self.input_text(self.exp_date_loc,exp_date)
		self.click(self.continue_buyFlights_loc)
