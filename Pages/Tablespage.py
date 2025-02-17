from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class TablePage(BasePage):
    SecondPg = (By.XPATH, '//button[.="2"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def go_to_second_page(self):
        self.driver.find_element(*self.SecondPg).click()
