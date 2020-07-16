#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, time, urllib.request, logging, re

# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#封装公共方法类
class Action(object):
    #初始化
    def __init__(self,selenium_driver):
        self.driver = selenium_driver

    #定义open方法
    def open(self,url):
        #cookies = self.driver.get_cookies()
        #self.driver.delete_all_cookies()
        self.driver.get(url)
        time.sleep(1)
        self.driver.maximize_window()
        logging.info(self.driver.title)
        #logging.debug("Chrome浏览器版本号: %s",self.driver.capabilities['version'])
        #Action(self.driver).close()
    
    def delete_cookies(self):
        cookies = self.driver.get_cookies()
        self.driver.delete_all_cookies()        
    
    #截图保存    
    def screenshot(self):
        test_method_name = self._testMethodName
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        screenshot_name = test_method_name+nowTime
        base_dir = sys.path[0]
        base = base_dir.split('\src\case')[0]
        self.driver.get_screenshot_as_file(base+"\\report\\screenshot\%s.png" %screenshot_name)
        print("http://191.168.30.184:8080/image/%s.png" %screenshot_name)
    
    #获取页面console.log()
    def browser_log(self,url):
        #enable浏览器记录
        d = DesiredCapabilities.CHROME 
        d ['loggingPrefs'] = {'browser':'ALL'} 
        self.driver = webdriver.Chrome(desired_capabilities=d)
        #加载网站
        self.driver.get(url)
        #打印信息
        for entry in self.driver.get_log('browser'):
            logging.info("%s",entry)

    #重写元素定位的方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            #Action.screenshot(self)
            logging.info("未找到元素:%s"%(self,loc))
            
    #重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    #重写switch_frame方法
    def switch_to_frame(self, *loc):
        return self.driver.switch_to_frame(*loc)

    
    #切换窗口
    def newwindows(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(1)
        logging.info(self.driver.title)
    
    
    #定义script方法，用于执行js脚本
    def script(self,src):
        self.driver.execute_script(src)
    
    #重写send_keys方法
    def send_keys(self,loc,value,clear_first=True,clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            logging.info("未找到%s"%(self,loc))
            
    def input_text(self,loc,text):
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)
        
    def click(self,loc):
        try:
            self.find_element(*loc).click()
        except AttributeError:
            logging.info("未找到%s"%(self,loc))
        
    def get_title(self):
        return self.driver.title
    
    def get_text(self,loc):
        logging.info("%s",self.find_element(*loc).text)
        return self.find_element(*loc).text
    
    #移动鼠标    
    def mouse_move(self,loc):
        target = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(target).perform()
        
    def mouse_click_right(self,loc):
        right = self.find_element(*loc)
        ActionChains(self.driver).context_click(right).perform()
        
    def mouse_click_left(self,loc):
        left = self.find_element(*loc)
        ActionChains(self.driver).click_and_hold(left).perform()

    #鼠标左键双击
    def double_click(self,loc):
        loc = self.find_element(*loc)
        ActionChains(self.driver).double_click(loc).perform()      
    
    #滚动鼠标到顶部   
    def mouse_top(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
    
    #滚动鼠标到底部   
    def mouse_bottom(self):
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)    

    #获取标签值
    def get_attribute(self,loc):
        #logging.info("name标签值：%s",self.find_element(*loc).get_attribute("name"))
        return self.find_element(*loc).get_attribute("name")
    
    #拖动到可见的元素
    def execute_script(self,loc):
        target = self.find_element(*loc)
        self.driver.execute_script("arguments[0].focus();",target)
        #self.driver.execute_script("arguments[0].scrollIntoView();",target)
    
    #tab键           
    def keys_tab(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.TAB)

    #回车键           
    def keys_enter(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.ENTER)

    #删除键           
    def keys_del(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.BACK_SPACE)

    #空格键           
    def keys_space(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.SPACE)

    #全选           
    def keys_a(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.CONTROL,'a')

    #复制           
    def keys_c(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.CONTROL,'c')

    #粘贴           
    def keys_v(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.CONTROL,'v')

    #剪切           
    def keys_x(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.CONTROL,'x')

    #回退键           
    def keys_espace(self,loc):
        target = self.find_element(*loc)
        target.send_keys(Keys.ESPACE)
        
    #模拟F12
    def F12(self):
        builder = ActionChains(self.driver)
        builder.key_down(Keys.F12).perform()
        
    def F5(self):
        builder = ActionChains(self.driver)
        builder.key_down(Keys.F5).perform()
        
    def refresh(self):
        self.driver.refresh()
        
    #关闭当前页面
    def close(self):
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(1)
        self.driver.close()
        time.sleep(1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(1)
        #logging.info(self.driver.title)
        
    #获取登录页面公钥
    def get_key(self,url):
        page = urllib.request.urlopen(url)
        #获取页面源码
        html = page.read()
        html = html.decode('utf-8')
        #print(html)
        #匹配的正则表达式
        #reg = r'securityKey" (.+?) type="hidden"'
        #reg = r'securityKey" value="(.+?)?="'
        reg = r'id="securityKey" value="(.+?)?="'
        value = re.search(reg,html)
        #print(value)
        #key = value.group(1).split('"')[1]
        key = value.group(1).split('"')[0]
        return key
    
    #直接input上传
    def upload_file(self,loc,file):
        #self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(file)

    #打开弹窗上传
    def upload_windows(self,loc,pwd):
        self.find_element(*loc).click()
        time.sleep(1)
        k=PyKeyboard()
        '''os.system(r"F:\\test.jpg")
        time.sleep(1)
        k.press_keys([k.control_key, 'c'])
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.press_keys([k.control_key, 'v'])
        time.sleep(1)'''
        k.type_string(pwd) 
        k.tap_key(k.enter_key)
        time.sleep(1)
        #python2可用
        '''SendKeys.SendKeys('F:\\test.jpg')  # 发送文件地址
        SendKeys.SendKeys("{ENTER}") # 发送回车键
        time.sleep(2)'''



    def clear(self,loc):
        self.find_element(*loc).clear()