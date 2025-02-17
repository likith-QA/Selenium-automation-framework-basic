import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from Pages.Modelpage import Modelpage
from Pages.Homepage import Homepage

class TestModals:

    # @pytest.mark.skip
    def test_simple_modal(self, driver):
        modal_page = Modelpage(driver)
        home_page = Homepage(driver)
        time.sleep(3)
        home_page.click_modals()
        modal_page.simplemo()

        try:
            modal_page.xmark()
            print("Test passed: Modal closed successfully.")
        except NoSuchElementException:
            print("Test failed: Modal did not close. Taking screenshot...")
            modal_page.take_screenshot("modal_close_failed.png")
            assert False, "Modal did not close properly."

    def test_complex_modal(self, driver):
        modal_page = Modelpage(driver)
        home_page = Homepage(driver)
        time.sleep(3)
        home_page.click_modals()
        modal_page.complexmo()
        modal_page.name_field("likith")
        modal_page.email_field("likith@gmail.com")
        modal_page.message_field("Hi")

        try:
            modal_page.submit_button()
            print("Test passed: Modal closed successfully.")
        except NoSuchElementException:
            print("Test failed: Modal did not close. Taking screenshot...")
            modal_page.take_screenshot("modal_close_failed.png")
            assert False, "Modal did not close properly."
