from selenium.webdriver.common.by import By
from Base.base_page import BasePage

class Homepage(BasePage):
    Delay = (By.XPATH, '//a[.="JavaScript Delays"]')
    Form = (By.XPATH, '//a[.="Form Fields"]')
    Popup = (By.XPATH, '//a[.="Popups"]')
    Slider = (By.XPATH, '//a[.="Sliders"]')
    Calendar = (By.XPATH, '//a[.="Calendars"]')
    Modals = (By.XPATH, '//a[.="Modals"]')
    Tables = (By.XPATH, '//a[.="Tables"]')
    WindowOp = (By.XPATH, '//a[.="Window Operations"]')
    Hover = (By.XPATH, '//a[.="Hover"]')
    Ads = (By.XPATH, '//a[.="Ads"]')
    Gesture = (By.XPATH, '//a[.="Gestures"]')
    FileDownload = (By.XPATH, '//a[.="File Download"]')
    Click = (By.XPATH, '//a[.="Click Events"]')
    Spinner = (By.XPATH, '//a[.="Spinners"]')
    Fileupload = (By.XPATH, '//a[.="File Upload"]')
    Iframes = (By.XPATH, '//a[.="Iframes"]')
    BrokenImg = (By.XPATH, '//a[.="Broken Images"]')
    BrokenLinks = (By.XPATH, '//a[.="Broken Links"]')
    Accordions = (By.XPATH, '//a[.="Accordions"]')

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage

    def click_delay(self):
        self.driver.find_element(*self.Delay).click()

    def click_form(self):
        self.driver.find_element(*self.Form).click()

    def click_popup(self):
        self.driver.find_element(*self.Popup).click()

    def click_slider(self):
        self.driver.find_element(*self.Slider).click()

    def click_calendar(self):
        self.driver.find_element(*self.Calendar).click()

    def click_modals(self):
        self.driver.find_element(*self.Modals).click()

    def click_tables(self):
        self.driver.find_element(*self.Tables).click()

    def click_window_operations(self):
        self.driver.find_element(*self.WindowOp).click()

    def click_hover(self):
        self.driver.find_element(*self.Hover).click()

    def click_ads(self):
        self.driver.find_element(*self.Ads).click()

    def click_gesture(self):
        self.driver.find_element(*self.Gesture).click()

    def click_file_download(self):
        self.driver.find_element(*self.FileDownload).click()

    def click_click_events(self):
        self.driver.find_element(*self.Click).click()

    def click_spinner(self):
        self.driver.find_element(*self.Spinner).click()

    def click_file_upload(self):
        self.driver.find_element(*self.Fileupload).click()

    def click_iframes(self):
        self.driver.find_element(*self.Iframes).click()

    def click_broken_images(self):
        self.driver.find_element(*self.BrokenImg).click()

    def click_broken_links(self):
        self.driver.find_element(*self.BrokenLinks).click()

    def click_accordions(self):
        self.driver.find_element(*self.Accordions).click()
