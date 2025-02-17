import time
from selenium.common import NoSuchElementException
from Pages.Homepage import Homepage
from Pages.Tablespage import TablePage

class TestTable:

    def test_page(self, driver):
        home_page = Homepage(driver)
        table_page = TablePage(driver)
        time.sleep(3)
        home_page.click_tables()

        try:
            time.sleep(3)
            table_page.go_to_second_page()
            print("Test passed: Navigated to second page successfully.")
        except NoSuchElementException:
            print("Test failed: Navigation failed. Taking screenshot...")
            table_page.take_screenshot("modal_close_failed.png")
            assert False, "Navigation properly."