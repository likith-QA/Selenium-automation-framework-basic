from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class IframePage(BasePage):
    Disney = (By.XPATH, '//a[@href="https://www.hotstar.com/"]')
    Search = (By.XPATH, '(//span[@class="LHDmaByQeS8uy1wgLgxz_"])[2]')
    Type = (By.XPATH, '//input[@id="searchBar"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_disney_image(self):
        self.driver.find_element(*self.Disney).click()

    def switch_to_iframe(self, iframe_locator):
        iframe = self.driver.find_element(*iframe_locator)
        self.driver.switch_to.frame(iframe)

    def search_icon(self):
        self.driver.find_element(*self.Search).click()

    def type(self):
        self.driver.find_element(*self.Type).send_keys()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()


