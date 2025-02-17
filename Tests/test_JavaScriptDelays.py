from selenium.common.exceptions import TimeoutException
from Pages.Delaypage import DelayPage

class TestJavaScriptDelays:

    def test_liftoff_message(self, driver):
        delay_page = DelayPage(driver)
        delay_page.delay_button()
        delay_page.click_start_button()

        try:
            assert delay_page.wait_for_liftoff_message(), "Liftoff! message not displayed."
            print("Test passed: 'Liftoff!' message appeared.")

        except (TimeoutException, AssertionError):
            print("Test failed: 'Liftoff!' message not found. Taking screenshot...")
            delay_page.take_screenshot("liftoff_not_appeared.png")
            raise  # Re-raise exception for test reporting

