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
        self.login(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Sign out").click()

    def login(self, wd):
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("technodeath@gmail.com")
        wd.find_element_by_id("passwd").clear()
        wd.find_element_by_id("passwd").send_keys("qwe123")
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
