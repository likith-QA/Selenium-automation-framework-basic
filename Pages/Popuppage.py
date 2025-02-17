from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class PopupPage(BasePage):
    AlertPopup = (By.XPATH, '//b[.="Alert Popup"]')
    ConfirmPopup = (By.XPATH, '//b[.="Confirm Popup"]')  # Fixed typo: Conform -> Confirm
    PromptPopup = (By.XPATH, '//b[.="Prompt Popup"]')
    Tooltip = (By.XPATH, '//div[@class="tooltip_1"]')


    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def click_alertpopup(self):
        self.driver.find_element(*self.AlertPopup).click()

    def click_confirmpopup(self):  # Fixed typo in method name
        self.driver.find_element(*self.ConfirmPopup).click()

    def click_promptpopup(self):
        self.driver.find_element(*self.PromptPopup).click()

    def click_tooltip(self):
        self.driver.find_element(*self.Tooltip).click()
