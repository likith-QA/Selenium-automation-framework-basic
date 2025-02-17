import time
import pytest
from selenium.common import NoSuchElementException
from Pages.Homepage import Homepage
from Pages.Windowspage import WindowsPage

class TestWindow:


    def test_new_window(self, driver):
        home_page = Homepage(driver)
        window_page = WindowsPage(driver)
        home_page.click_window_operations()
        time.sleep(5)
        initial_tabs = driver.window_handles
        time.sleep(2)
        window_page.open_new_window()
        time.sleep(2)

        try:
            # Check if a new tab is opened
            new_tabs = driver.window_handles
            assert len(new_tabs) > len(initial_tabs), "New tab did not open."
            print("Test passed: New tab opened successfully.")

        except (NoSuchElementException, AssertionError) as e:
            print("Test failed: No new tab opened. Taking screenshot...")
            window_page.take_screenshot("new_tab_failed.png")
            raise e


    def test_replace(self, driver):
        home_page = Homepage(driver)
        window_page = WindowsPage(driver)

        time.sleep(3)
        home_page.click_window_operations()
        initial_url = driver.current_url
        window_page.open_replace_window()
        time.sleep(3)

        try:
            new_url = driver.current_url
            assert new_url != initial_url, "URL did not change after opening replace window."
            print("Test passed: URL changed successfully.")

        except AssertionError:
            print("Test failed: URL did not change. Taking screenshot...")
            window_page.take_screenshot("replace_window_failed.png")
            raise

    def test_new_tab(self, driver):
        home_page = Homepage(driver)
        window_page = WindowsPage(driver)
        home_page.click_window_operations()
        time.sleep(5)
        initial_tabs = driver.window_handles
        time.sleep(2)
        window_page.open_new_tab()
        time.sleep(2)

        try:

            new_tabs = driver.window_handles
            assert len(new_tabs) > len(initial_tabs), "New tab did not open."
            print("Test passed: New tab opened successfully.")

        except (NoSuchElementException, AssertionError) as e:
            print("Test failed: No new tab opened. Taking screenshot...")
            window_page.take_screenshot("new_tab_failed.png")
            raise e