from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Base.base_page import BasePage

class FileUploadPage(BasePage):
    FileUpload = (By.XPATH, '//input[@id="file-upload"]')
    UploadButton = (By.XPATH, '//input[@id="upload-btn"]')
    Conformation = (By.XPATH, '//div[@class="wpcf7-response-output"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def upload_file(self, file_path):
        self.driver.find_element(*self.FileUpload).send_keys(file_path)

    def click_upload_button(self):
        self.driver.find_element(*self.UploadButton).click()

    def conformation(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.Conformation)
            )
            return True
        except TimeoutException:
            return False
