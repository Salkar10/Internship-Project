
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Page:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver
        driver.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def input_text(self, EMAIL, email):
        pass

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    #def get_element(self, *locator):

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def find_elements_by_id(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator: object) -> None:
        self.driver.find_element(*locator).click()


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Expected {expected_text}, but got {actual_text}'

    def wait_until_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f'Element by {locator} not clickable.'
        ).click()

    def wait_until_element_appear(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(*locator),
            message=f'Element by {locator} did not appear.'
        )
        return element

    #def input_text(self, *locator, text):
        #self.driver.find_element(*locator).clear()
        #self.driver.find_element(*locator).send_keys(text)

    #def input_text(self, *locator, text):
        #element = self.driver.find_element(*locator)
        #element.clear()
        #element.send_keys(text)

    def input_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)