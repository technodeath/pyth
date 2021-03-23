from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def find_item_on_site(self, item):
        wd = self.wd
        wd.find_element_by_id("search_query_top").send_keys(item)
        wd.find_element_by_css_selector("button[name='submit_search']").click()

    def click_on_item(self, item):
        wd = self.wd
        wd.find_element_by_css_selector("a[title='%s']" % item).click()

    def click_add_to_cart(self):
        wd = self.wd
        wd.find_element_by_id("add_to_cart").click()

    def click_close_popup(self):
        wd = self.wd
        wd.find_element_by_css_selector("span.cross").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://automationpractice.com/index.php")

    def destroy(self):
        self.wd.quit()