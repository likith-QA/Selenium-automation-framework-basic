import time
from Pages.Homepage import Homepage
from Pages.Clickpage import ClickPage

class TestClick:

    def test_cat(self, driver):
        home_page = Homepage(driver)
        click_page = ClickPage(driver)

        time.sleep(5)
        home_page.click_click_events()
        click_page.click_cat()

        time.sleep(2)

        if click_page.cat_conf():
            print("Test Passed: Cat confirmation appeared. No screenshot needed.")
        else:
            print("Test Failed: Cat confirmation did not appear. Taking screenshot...")
            click_page.take_screenshot("cat_confirmation_failed.png")
            raise AssertionError("Cat confirmation message did not appear.")
