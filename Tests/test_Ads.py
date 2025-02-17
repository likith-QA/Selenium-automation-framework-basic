from Pages.Homepage import Homepage
from Pages.Adspage import AdsPage
import time
from selenium.common.exceptions import NoSuchElementException

class TestAds:

    def test_ads(self, driver):
        home_page = Homepage(driver)
        ads_page = AdsPage(driver)

        time.sleep(5)
        home_page.click_ads()
        time.sleep(5)

        ads_page.close_ad()
        time.sleep(2)
        if ads_page.is_ad_present():
            print("Test Failed: Ad did not close. Taking screenshot...")
            ads_page.take_screenshot("ad_not_closed.png")
            raise AssertionError("Ad did not close properly.")
        else:
            print("Test Passed: Ad successfully closed.")
