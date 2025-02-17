import time

import pytest

from Pages.Homepage import Homepage
from Pages.Iframespage import IframePage

class Testframe:

    def test_frame(self, driver):
        home_page = Homepage(driver)
        frame_page = IframePage(driver)
        time.sleep(5)
        home_page.click_iframes()
        time.sleep(10)
        frame_page.click_disney_image()
        frame_page.switch_to_iframe(1)
        frame_page.search_icon()
        frame_page.enter_text("Avengers")
