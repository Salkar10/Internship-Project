from pages.base_page import Page
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage



class Application:

    def __init__(self,driver):
        self.base_page = Page(driver)
        self.driver = driver
        self.page = Page(driver)
        self.login_page = LoginPage(driver)
        self.off_plan_page=OffPlanPage(driver)

