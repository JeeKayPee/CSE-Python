import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.base_test_2 import BaseTest2
from common.config import Configuration


class CSETest(BaseTest2):
    def test_(self):
        self.driver.find_element(By.LINK_TEXT, "Media").click()
        self.driver.find_element(By.LINK_TEXT, "Add New").click()

        browse_button = self.driver.find_element(By.ID, "async-upload")
        file_path = Configuration.get_upload_file_path("file-upload.jpg")

        browse_button.send_keys(file_path)

        self.driver.find_element(By.ID, "html-upload").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "thumbnail")))

        # We can take further actions to verify correct file upload. Skipping for this exercise


if __name__ == '__main__':
    unittest.main()
