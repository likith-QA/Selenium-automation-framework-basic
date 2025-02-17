from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Base.base_page import BasePage

class FormPage(BasePage):
    NameField = (By.ID, 'name-input')
    Password = (By.XPATH, '//input[@type="password"]')
    WaterCheckbox = (By.XPATH, '//input[@id="drink1"]')
    ColorField = (By.XPATH, '//input[@id="color1"]')
    DropDown = (By.NAME, 'automation')
    Option = "Yes"
    EmailField = (By.XPATH, '//input[@id="email"]')
    MessageField = (By.ID, 'message')
    SubmitButton = (By.ID, 'submit-btn')
    ConfirmationMessage = (By.XPATH, '//p[.="Message received!"]')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self, name):
        self.driver.find_element(*self.NameField).send_keys(name)

    def enter_password(self, password):
        self.driver.find_element(*self.Password).send_keys(password)

    def select_water_checkbox(self):
        checkbox = self.driver.find_element(*self.WaterCheckbox)
        if not checkbox.is_selected():
            checkbox.click()

    def select_color(self):
        self.driver.find_element(*self.ColorField).click()

    def select_dropdown_option(self):
        dropdown = Select(self.driver.find_element(*self.DropDown))
        dropdown.select_by_visible_text(self.Option)

    def enter_email(self, email):
        self.driver.find_element(*self.EmailField).send_keys(email)

    def enter_message(self, message):
        self.driver.find_element(*self.MessageField).send_keys(message)

    def submit_form(self):
        self.driver.find_element(*self.SubmitButton).click()

    def is_confirmation_message_present(self, expected_text):
        try:
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ConfirmationMessage)
            )
            return message_element.text == expected_text
        except TimeoutException:
            return False
