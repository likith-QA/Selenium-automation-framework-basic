import time
import pytest
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from Pages.Popuppage import PopupPage
from Pages.Homepage import Homepage

class TestPopup:

    # @pytest.mark.skip
    def test_alert_popup(self, driver):
        home_page = Homepage(driver)
        popup_page = PopupPage(driver)
        time.sleep(3)
        home_page.click_popup()
        popup_page.click_alertpopup()

        try:
            # Switch to alert and verify the message
            alert = driver.switch_to.alert
            message = alert.text

            assert "Hi there, pal!" in message, "Confirmation message not found in alert."

            print("Test Passed: 'Hi there, pal!' appeared in alert.")
            alert.accept()  # Click OK
        except (NoAlertPresentException, AssertionError):
            print("Test Failed: Alert not found or incorrect message. Taking screenshot...")
            popup_page.take_screenshot("popup_failed.png")
            raise

    # @pytest.mark.skip
    def test_confirm_popup_accept(self, driver):
        home_page = Homepage(driver)
        popup_page = PopupPage(driver)
        time.sleep(3)
        home_page.click_popup()
        popup_page.click_confirmpopup()

        try:
            alert = driver.switch_to.alert  # Switch to the popup
            message = alert.text  # Get the popup message
            print(f"Confirm Popup Message: {message}")

            assert "OK or Cancel, which will it be?" in message, "Unexpected confirm popup message!"

            alert.accept()
            # alert.dismiss()
            print("Test Passed: Clicked OK on the confirm popup.")
            # print("Test Passed: Clicked Cancel on the confirm popup.")

        except NoAlertPresentException:
            print("Test Failed: Confirm popup did not appear. Taking screenshot...")
            popup_page.take_screenshot("confirm_popup_failed.png")
            raise

    def test_prompt_popup(self, driver):
        home_page = Homepage(driver)
        popup_page = PopupPage(driver)
        time.sleep(3)
        home_page.click_popup()
        popup_page.click_promptpopup()

        try:
            alert = driver.switch_to.alert
            print(f"Prompt Popup Message: {alert.text}")

            alert.send_keys("Hello, Selenium!")
            alert.accept()
            # alert.dismiss()
            print("Test Passed: Entered text and clicked OK on the prompt popup.")

        except NoAlertPresentException:
            print("Test Failed: Prompt popup did not appear. Taking screenshot...")
            popup_page.take_screenshot("prompt_popup_failed.png")
            raise

