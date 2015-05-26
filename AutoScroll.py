#coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import urllib

import unittest, time, re

canshu= 'Beijing lang:en since:2014-01-01 until:2015-01-01'#搜索参数
#daili= '124.202.175.70'#代理url
#duankou= 8001#整数类型，代理端口


www = 'https://twitter.com/search?'#主页面



#构造请求参数，f表示所有twitters.
query = urllib.urlencode(dict(q=canshu,
                              sec='typd',
                              vertical='default',
                              f='tweets',
                              ))

#设定内置浏览器禁止加载图片
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image',2)
firefox_profile.set_preference('permissions.default.stylesheet',2)#禁用css


#firefox_profile.set_preference('network.proxy.type',1)#参数1说明手动配置代理，0表示直接连接。
#firefox_profile.set_preference('network.proxy.http',daili)#代理url
#firefox_profile.set_preference('network.proxy.http_port',duankou)#代理url端口
#firefox_profile.set_preference('network.proxy.ssl',daili)#代理url针对https网站
#firefox_profile.set_preference('network.proxy.ssl_port',duankou)#代理urlssl端口
#firefox_profile.update_preferences()




class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_profile=firefox_profile)#实例化火狐并添加禁止图片css设定。
        self.driver.implicitly_wait(30)
        self.base_url = www
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url + query)
        #driver.find_element_by_link_text("All").click()
        for i in range(1,1000):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')


if __name__ == "__main__":
    unittest.main()
