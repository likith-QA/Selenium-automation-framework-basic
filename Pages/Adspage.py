from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Base.base_page import BasePage

class AdsPage(BasePage):
    AdCloseButton = (By.XPATH, '(//button[@aria-label="Close"])[1]')
    AdContainer = (By.XPATH, '//div[@id="popmake-1272"]')

    def __init__(self, driver):
        super().__init__(driver)

    def close_ad(self):
        self.driver.find_element(*self.AdCloseButton).click()

    def is_ad_present(self):
        try:
            ad_element = self.driver.find_element(*self.AdContainer)
            return ad_element.is_displayed()  # Return False if it's hidden
        except NoSuchElementException:
            return False
