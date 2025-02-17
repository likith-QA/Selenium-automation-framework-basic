from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Base.base_page import BasePage
import time


class GesturePage(BasePage):
    FromElement = (By.XPATH, '//div[@id="div1"]')
    ToElement = (By.XPATH, '//div[@id="div2"]')

    def __init__(self, driver):
        super().__init__(driver)

    def drag_and_drop(self):
        from_element = self.driver.find_element(*self.FromElement)
        to_element = self.driver.find_element(*self.ToElement)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(from_element, to_element).perform()
        time.sleep(2)
