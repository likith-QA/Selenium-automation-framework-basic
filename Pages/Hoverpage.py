from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Base.base_page import BasePage

class HoverPage(BasePage):
    HoverElement = (By.XPATH, '//h3[.="Mouse over me"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def hover_over_element(self):
        hover_element = self.driver.find_element(*self.HoverElement)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()

        # Try retrieving tooltip or confirmation message
        try:
            message = hover_element.get_attribute("title")  # Check if it's a tooltip
            if not message:
                message = self.driver.execute_script("return arguments[0].textContent;", hover_element)
            return message
        except Exception:
            return None
