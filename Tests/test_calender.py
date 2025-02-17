import time
from Pages.Calenderpage import CalenderPage
from Pages.Homepage import Homepage

class TestCalender:

    def test_calender(self, driver):
        home_page = Homepage(driver)
        calender_page = CalenderPage(driver)

        home_page.click_calendar()
        calender_page.enter_date("2024-02-10")
        calender_page.click_sc()
        calender_page.submit_button()

        # Capture current page state before waiting
        old_page_source = driver.page_source  

        time.sleep(5)  # Wait for refresh

        # Check if the page refreshed
        if driver.page_source == old_page_source:  
            print("Test failed: Page did not refresh. Taking screenshot...")
            calender_page.take_screenshot("page_not_refreshed.png")
        else:
            print("Test passed: Page refreshed successfully.")
