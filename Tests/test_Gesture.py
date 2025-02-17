from Pages.Homepage import Homepage
from Pages.Gesturepage import GesturePage
import time
from selenium.common.exceptions import WebDriverException

class TestGesture:

    def test_dragdrop(self, driver):
        home_page = Homepage(driver)
        gesture_page = GesturePage(driver)

        time.sleep(5)
        home_page.click_gesture()

        try:
            gesture_page.drag_and_drop()
            print("Test Passed: Drag and Drop was successful.")
        except WebDriverException:
            print("Test Failed: Drag and Drop did not occur. Taking screenshot...")
            gesture_page.take_screenshot("dragdrop_failed.png")
            raise
