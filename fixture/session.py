class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Sign out").click()

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Sign in").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_id("passwd").clear()
        wd.find_element_by_id("passwd").send_keys(password)
        wd.find_element_by_xpath("//button[@id='SubmitLogin']/span").click()