from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Sign out").click()

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

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_id("passwd").clear()
        wd.find_element_by_id("passwd").send_keys(password)
        wd.find_element_by_xpath("//button[@id='SubmitLogin']/span").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://automationpractice.com/index.php")

    def destroy(self):
        self.wd.quit()