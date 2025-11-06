from selenium.webdriver.common.by import By
from pages.base_page import Page
class LoginPage(Page):


    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button.w-button')



    def open_login_page(self, url):
        self.open_url(url)

    def user_login(self, email, password):
        self.input_text(self.EMAIL, email)
        self.input_text(self.PASSWORD, password)
        #self.click(self.LOGIN_BTN)
        self.click(*self.LOGIN_BTN)

    def is_login_successful(self):
        """Verify login was successful"""
        try:
            self.driver.implicitly_wait(5)
            return "login" not in self.driver.current_url.lower()
        except:
            return False


