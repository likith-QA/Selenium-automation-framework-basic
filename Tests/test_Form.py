import time
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from Pages.Homepage import Homepage
from Pages.Formpage import FormPage

class TestForm:

    # @pytest.mark.skip
    def test_testform(self, driver):
        form_page = FormPage(driver)
        home_page = Homepage(driver)
        time.sleep(3)
        home_page.click_form()
        form_page.enter_name("likith")
        form_page.enter_password("123")
        form_page.select_water_checkbox()
        form_page.select_color()
        form_page.select_dropdown_option()
        form_page.enter_email("likith@gmail.com")
        form_page.enter_message("Hello")
        time.sleep(2)
        form_page.submit_form()

        try:
            alert = driver.switch_to.alert
            message = alert.text
            assert "Message received!" in message, "Confirmation message not found in alert."
            print("Test Passed: 'Message received!' appeared in alert.")

            # Accept the alert (click OK)
            alert.accept()

        except (NoAlertPresentException, AssertionError):
            print("Test Failed: Alert not found or incorrect message. Taking screenshot...")
            form_page.take_screenshot("form_submission_failed.png")
            raise

