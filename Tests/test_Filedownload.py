import pytest
from Pages.Homepage import Homepage
from Pages.Filedownloadpage import FileDownloadPage
from time import sleep
from selenium.common.exceptions import WebDriverException, NoSuchElementException

class TestFileDownload:

    # @pytest.mark.skip
    def test_file1(self, driver):
        home_page = Homepage(driver)
        file_page = FileDownloadPage(driver)

        sleep(5)
        home_page.click_file_download()

        try:
            file_page.download_file_1()
            print("Test Passed: File 1 download started successfully.")
        except WebDriverException:
            print("Test Failed: File 1 did not start downloading. Taking screenshot...")
            file_page.take_screenshot("file1_download_failed.png")
            raise

    @pytest.mark.xfail
    def test_file2(self, driver):
        home_page = Homepage(driver)
        file_page = FileDownloadPage(driver)

        sleep(3)
        home_page.click_file_download()
        sleep(2)

        try:
            file_page.click_word_file_download()
            sleep(3)

            file_page.enter_password("automateNow")
            file_page.submit_password()
            sleep(3)

            print("Test Passed: Word file download started successfully.")

        except (WebDriverException, NoSuchElementException):
            print("Test Failed: File did not start downloading. Taking screenshot...")
            file_page.take_screenshot("file_download_failed.png")
            raise
