# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def test_login(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="technodeath@gmail.com", password="qwe123")
        self.find_item_on_site(wd, item="Blouse")
        self.click_on_item(wd, item="Blouse")
        self.click_add_to_cart(wd)
        self.click_close_popup(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Sign out").click()

    def find_item_on_site(self, wd, item):
        wd.find_element_by_id("search_query_top").send_keys(item)
        wd.find_element_by_css_selector("button[name='submit_search']").click()

    def click_on_item(self, wd, item):
        wd.find_element_by_css_selector("a[title='%s']" % item).click()

    def click_add_to_cart(self, wd):
        wd.find_element_by_id("add_to_cart").click()

    def click_close_popup(self, wd):
        wd.find_element_by_css_selector("span.cross").click()

    def login(self, wd, username, password):
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_id("passwd").clear()
        wd.find_element_by_id("passwd").send_keys(password)
        wd.find_element_by_xpath("//button[@id='SubmitLogin']/span").click()

    def open_home_page(self, wd):
        wd.get("http://automationpractice.com/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
