#coding=utf-8
import os
import json


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.proxy import *


import sys

import unittest, time, re


import json
import urllib
import urllib2



canshu= 'Shanghai lang:en since:2014-01-01 until:2015-01-01'#搜索参数
#daili= '82.222.61.111'#代理url
#duankou= 443#整数类型，代理端口
#myproxy = '82.222.61.111:443'
#proxy = Proxy({
#'proxyType':ProxyType.MANUAL,
#'httpProxy':myproxy,
#'sslProxy':myproxy,
#'ftpProxy':myproxy,
#'noProxy':''
#})





www = 'https://twitter.com/i/search/timeline?'#主页面
mimi =''

query =urllib.urlencode(dict(q='Beijing lang:en since:2014-01-01 until:2014-12-31',
                             src='typd',
                             include_entities=1,
                             #scroll_cursor = 'TWEET-549520628957458432-550078740466651136-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                             vertical='default',
                             include_available_features=1,
                             composed_count=0,
                             f='tweets',
                             include_new_items_bar='true',
                             interval=30000,
                             latent_count=0,
                             ))


#设定内置浏览器禁止加载图片
firefox_profile = webdriver.FirefoxProfile()#'/Users/chengang/Desktop/profile/'
firefox_profile.set_preference('permissions.default.image',2)
firefox_profile.set_preference('permissions.default.stylesheet',2)#禁用css
#firefox_profile.set_preference('javascript.enabled',false)#禁用 js

#自动保存文件
firefox_profile.set_preference('browser.download.folderList',2)#2询问下载位置，1下载目录，0桌面
firefox_profile.set_preference('browser.download.manager.showWhenStarting',False)
firefox_profile.set_preference('browser.download.dir', '~/Document')
firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/json')

#firefox_profile.set_preference('network.proxy.type',1)#参数1说明手动配置代理，0表示直接连接。
#firefox_profile.set_preference('network.proxy.http',daili)#代理url
#firefox_profile.set_preference('network.proxy.http_port',duankou)#代理url端口
#firefox_profile.set_preference('network.proxy.ssl',daili)#代理url针对https网站
#firefox_profile.set_preference('network.proxy.ssl_port',duankou)#代理urlssl端口
##firefox_profile.set_preference('setAssumeUntrustedCertificateIssuer', False)
##firefox_profile.set_preference('setAcceptUntrustecCertificats',True)
#
#firefox_profile.set_preference('webdriver_assume_untrusted_issuer', False)
#firefox_profile.set_preference('webdriver_accept_untrusted_certs',True)
#firefox_profile.accept_untrusted_certs = True
#
#
#firefox_profile.set_preference('general.useragent.override','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4')



#firefox_profile.set_preference('webdriver_assume_untrusted_issuer', True);
#firefox_profile.set_preference('webdrive_accept_untrusted_certs', True)


firefox_profile.update_preferences()



#chrome_options = webdriver.ChromeOptions()
#prefs ={
#        'disable_popup_blocking':True,
#        'download.prompt_for_download':False,
#        'download.default_directory': '~/Document',
#        'download.directory_upgrade': True,
#        'profile.default_content_setting.popups': 0,
#        }
#
#
#
#chrome_options.add_experimental_option('prefs', prefs)
#chrome_options.add_argument('--proxy-server=http://%s' % proxy)






'''proxy=proxy,'''

driver = webdriver.Firefox(firefox_profile=firefox_profile)#实例化火狐并添加禁止图片css设定。
#driver = webdriver.Chrome(executable_path='/Users/chengang/Downloads/chromedriver',chrome_options=chrome_options)
#driver.implicitly_wait(30)
#driver.delete_all_cookies()#清空浏览器cookie
driver.get(www+ query)
time.sleep(2)

jsonfile = open('/Users/chengang/Document/json.json').read()
driver.implicitly_wait(6)
time.sleep(2)

data = json.loads(jsonfile.decode('utf-8-sig'))
for i in data.items():
    if i[0] == "scroll_cursor":
        global mimi
        mimi = i[1]
        print mimi
driver.quit()
time.sleep(2)





z =1
while 1:

    query2 =urllib.urlencode(dict(q='Beijing lang:en since:2014-01-01 until:2014-12-31',
                                  src='typd',
                                  include_entities=1,
                                  scroll_cursor = mimi,
                                  vertical='default',
                                  include_available_features=1,
                                  composed_count=0,
                                  f='tweets',
                                  include_new_items_bar='true',
                                  interval=30000,
                                  latent_count=0,
                                  ))

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image',2)
    firefox_profile.set_preference('permissions.default.stylesheet',2)#禁用css
    #firefox_profile.set_preference('javascript.enabled',false)#禁用 js

    #自动保存文件
    firefox_profile.set_preference('browser.download.folderList',2)#2询问下载位置，1下载目录，0桌面
    firefox_profile.set_preference('browser.download.manager.showWhenStarting',False)
    firefox_profile.set_preference('browser.download.dir', '~/Document')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/json')




    driver = webdriver.Firefox(firefox_profile=firefox_profile)#实例化火狐并添加禁止图片css设定。

    driver.set_window_position(1400,100)#设定窗口位置
    driver.set_window_size(3,3)#设定窗口大小



    #self.driver = webdriver.Chrome()
    driver.implicitly_wait(300)
    driver.delete_all_cookies()#清空浏览器cookie
    driver.get(www+ query2)
    time.sleep(2)

    jsonfile = open('/Users/chengang/Document/json('+str(z)+').json').read()
    time.sleep(2)
    z = z+1
    driver.implicitly_wait(6)

    data = json.loads(jsonfile.decode('utf-8-sig'))
    for n in data.items():
        if n[0] == "scroll_cursor":
            global mimi
            mimi = n[1]
            print mimi
    driver.close()
    time.sleep(2)

