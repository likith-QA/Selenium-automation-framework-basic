from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Base.base_page import BasePage

class ClickPage(BasePage):
    Cat = (By.XPATH, '//button[.="Cat"]')
    Catconf = (By.XPATH, '//h2[.="Meow!"]')
    Dog = (By.XPATH, '//button[.="Dog"]')
    Dogconf = (By.XPATH, '//h2[.="Woof!"]')
    Cow = (By.XPATH, '//button[.="Cow"]')
    Cowconf = (By.XPATH, '//h2[.="Moo!"]')
    Pig = (By.XPATH, '//button[.="Pig"]')
    Pigconf = (By.XPATH, '//h2[.="Oink!"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_cat(self):
        self.driver.find_element(*self.Cat).click()

    def cat_conf(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.Catconf)
            )
            return True
        except TimeoutException:
            return False

    def click_dog(self):
        self.driver.find_element(*self.Dog).click()

    def dog_conf(self):
        self.driver.find_element(*self.Dogconf)

    def click_cow(self):
        self.driver.find_element(*self.Cow).click()

    def cow_conf(self):
        self.driver.find_element(*self.Cowconf)

    def click_pig(self):
        self.driver.find_element(*self.Pig).click()

    def pig_conf(self):
        self.driver.find_element(*self.Pigconf)
