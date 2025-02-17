from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class CalenderPage(BasePage):
    DateField = (By.XPATH, '//input[@class="date jp-contact-form-date grunion-field hasDatepicker"]')
    SubmitButton = (By.XPATH, '(//button[.="Submit"])[1]')
    ClickSc = (By.XPATH, '//div[@class="copyright-text text-center"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def enter_date(self, date):
        self.driver.find_element(*self.DateField).send_keys(date)

    def submit_button(self):
        self.driver.find_element(*self.SubmitButton).click()

    def click_sc(self):
        self.driver.find_element(*self.ClickSc).click()
