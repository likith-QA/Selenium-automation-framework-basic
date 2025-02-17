from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.Homepage import Homepage
from Base.base_page import BasePage  # Import BasePage for common methods

class DelayPage(BasePage):
    StartButton = (By.XPATH, '//b[.="Start"]')
    Countdown = (By.XPATH, '(//input[@type="text"])[1]')  # Locator for countdown input field

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def delay_button(self):
        self.driver.find_element(*Homepage.Delay).click()

    def click_start_button(self):
        self.driver.find_element(*self.StartButton).click()

    def wait_for_liftoff_message(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.text_to_be_present_in_element_value(self.Countdown, "Liftoff!")
            )
            return True
        except TimeoutException as e:
            print(f"Timeout waiting for Liftoff! message: {e}")
            self.take_screenshot("Liftoff_Failure")  # Call take_screenshot from BasePage
            return False

