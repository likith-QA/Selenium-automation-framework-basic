from Pages.Homepage import Homepage
from Pages.Hoverpage import HoverPage
import time

class TestHover:

    def test_hover(self, driver):
        hover_page = HoverPage(driver)
        home_page = Homepage(driver)

        home_page.click_hover()
        time.sleep(5)
        message = hover_page.hover_over_element()

        if message and "You did it!" in message:
            print("Test Passed: Hover confirmation message appeared.")
        else:
            print("Test Failed: No confirmation message found. Taking screenshot...")
            hover_page.take_screenshot("hover_failed.png")
            raise AssertionError("Hover confirmation message not found.")
