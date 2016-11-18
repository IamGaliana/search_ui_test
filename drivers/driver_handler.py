#! /usr/bin/evn python
# encoding: utf8
__author__ = 'gaoyanjun'

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from src.utils.log_handler import *


class DriverHandler(object):

    def __init__(self, browser_type="FireFox"):
        if browser_type.lower() == 'ie':
            self.driver = webdriver.Ie()
        elif browser_type.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser_type.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 打开url
    def goto(self, url):
        try:
            goto = self.driver.get(url)
        except Exception, e:
            log_error("url not reached, exception: %s" % e.message)
        return goto

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 截图
    def screen_shot(self, url, filename):
        self.driver.get(url)
        self.driver.save_screenshot(filename)
        self.driver.quit()

    # 最大化浏览器窗口
    def max_window(self):
        self.driver.maximize_window()

    # 获得当前的url地址
    def get_current_url(self):
        return self.driver.current_url

    # 获得cookie信息
    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    # 删除所有cookie
    def delete_cookies(self):
        self.driver.delete_all_cookies()

    # 删除指定cookie
    def delete_cookie_by_name(self, name):
        self.driver.delete_cookie(name)

    # 等待页面元素加载
    def wait_for_element_load(self, element, timeout=30):
        locator = self.get_element_locator(element)
        try:
            element = element.split('->')
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except Exception, e:
            log_error("Element %s not found, exception: %s" % (element, e.message))
        return element

    # 获取页面元素
    def get_element_locator(self, element):
        element_locator = ()
        element = element.split('->')
        if element[0].lower() == 'id':
            element_locator = (By.ID, element[-1])
        elif element[0].lower() == 'xpath':
            element_locator = (By.XPATH, element[-1])
        return element_locator

    # 根据xpath或id找到某个元素
    def find_element(self, element, timeout=30):
        element = self.wait_for_element_load(element, timeout)
        element = self.driver.find_element(by=element[0], value=element[-1])
        return element

    # 找到元素列表
    def find_elements_list(self, element, timeout=30):
        element = self.wait_for_element_load(element, timeout)
        element_list = self.driver.find_elements(by=element[0], value=element[-1])
        return element_list

    # 写入textbox
    def send_keys(self, element, content, timeout=30):
        element = self.wait_for_element_load(element, timeout)
        try:
            element = self.driver.find_element(by=element[0], value=element[-1])
            element.clear()
            element.send_keys(content)
        except Exception, e:
            log_error("value not sent to text box, exception: %s" % e.message)

    # 判断元素是否存在
    def is_element_exist(self, element, timeout=30):
        # element = self.wait_for_element_load(element, timeout)
        element = element.split("->")
        try:
            self.driver.find_element(by=element[0], value=element[-1])
        except NoSuchElementException, e:
            log_error("NoSuchElementException: %s" % e.message)
            return False
        return True

    # 点击页面元素
    def click(self, element, timeout=30):
        element = self.wait_for_element_load(element, timeout)
        try:
            self.driver.find_element(by=element[0], value=element[-1]).click()
            time.sleep(3)
        except Exception, e:
            log_error(" - [search_common] - [click] - element not clicked, exception: %s" % e.message)

    # 获取元素属性值
    def get_attribute(self, element, name):
        element = self.wait_for_element_load(element)
        return self.driver.find_element(by=element[0], value=element[-1]).get_attribute(name)

    # 获得页面元素的text
    def text(self, element):
        element = self.wait_for_element_load(element)
        return self.driver.find_element(by=element[0], value=element[-1]).text

    # 鼠标hover
    def mouse_hover(self, element):
        element = self.wait_for_element_load(element)
        a = self.driver.find_element(by=element[0], value=element[-1])
        obj = ActionChains(self.driver).move_to_element(a)
        time.sleep(2)
        obj.perform()
        #ActionChains(self.driver).move_to_element(a).perform()

    # 选择下拉列表中的一项，choice可以是下拉列表项的text也可以是数字索引
    # 示例：action.select("xpath->.//*[@id='pos_id']/option", u"全部分类")
    def select(self, element, choice):
        element = self.wait_for_element_load(element)
        all_options = self.driver.find_elements(by=element[0], value=element[-1])
        chosen = None
        for i in xrange(len(all_options)):
            if choice == all_options[i].text:
                chosen = i
            elif choice == i:
                chosen = i
        try:
            all_options[chosen].click()
        except Exception, e:
            log_error("没有该选项, exception: %s" % e.message)
