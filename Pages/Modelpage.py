from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class Modelpage(BasePage):
    SimpleMo = (By.XPATH, '//button[.="Simple Modal"]')
    Xmark = (By.XPATH, '(//button[@class="pum-close popmake-close"])[2]')

    ComplexMo = (By.XPATH, '//button[.="Form Modal"]')
    Namefield = (By.XPATH, '//input[@type="text"]')
    Emailfield = (By.XPATH, '//input[@type="email"]')
    Messagefields = (By.XPATH, '//textarea[@name="g1051-message"]')
    Submitbutton = (By.XPATH, '//button[.="Submit"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def simplemo(self):
        self.driver.find_element(*self.SimpleMo).click()

    def xmark(self):
        self.driver.find_element(*self.Xmark).click()

    def complexmo(self):
        self.driver.find_element(*self.ComplexMo).click()

    def name_field(self, name):
        self.driver.find_element(*self.Namefield).send_keys(name)

    def email_field(self, email):
        self.driver.find_element(*self.Emailfield).send_keys(email)

    def message_field(self, message):
        self.driver.find_element(*self.Messagefields).send_keys(message)

    def submit_button(self):
        self.driver.find_element(*self.Submitbutton).click()

