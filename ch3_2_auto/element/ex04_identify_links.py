import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.selenium_utils import print_element_info


class CSETest(BaseTest1):

    # Identify Lost your password link by Full text

    def test_01(self):
        element = self.driver.find_element(By.LINK_TEXT, "Lost your password?")
        print_element_info("Lost Password link", element)

    # Identify <-Back to blog by Partial Link Text
    # (contains <- and the name of the blog can change with blog

    def test_02(self):
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Back to")
        print_element_info("Lost Password link", element)


if __name__ == '__main__':
    unittest.main()
