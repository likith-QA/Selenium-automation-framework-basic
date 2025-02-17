from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class FileDownloadPage(BasePage):
    D1 = (By.XPATH, '(//a[.="Download"])[1]')
    D2 = (By.XPATH, '(//a[.="Download"])[2]')
    PwdField = (By.XPATH, '//input[@placeholder="Enter Password"]')
    SubmitButton = (By.XPATH, '//input[@value="Submit"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def download_file_1(self):
        self.driver.find_element(*self.D1).click()

    def click_word_file_download(self):
        self.driver.find_element(*self.D2).click()

    def enter_password(self, password):
        self.driver.find_element(*self.PwdField).send_keys(password)

    def submit_password(self):
        self.driver.find_element(*self.SubmitButton).click()
