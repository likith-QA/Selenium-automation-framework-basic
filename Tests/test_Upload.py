import time
from Pages.Homepage import Homepage
from Pages.Fileuploadpage import FileUploadPage
from time import sleep

class Testupload:

    def test_upload(self, driver):
        home_page = Homepage(driver)
        upload_page = FileUploadPage(driver)
        home_page.click_file_upload()
        time.sleep(5)
        upload_page.upload_file("C:/Users/Tech/PycharmProjects/PythonProject/TestData/file-example_PDF_500_kB.pdf")
        upload_page.click_upload_button()
        # time.sleep(5)

        if upload_page.conformation():
            print("Test Passed: File uploaded successfully. No screenshot needed.")
        else:
            print("Test Failed: No confirmation message appeared. Taking screenshot...")
            upload_page.take_screenshot("file_upload_failed.png")
            raise AssertionError("File upload confirmation message did not appear.")
