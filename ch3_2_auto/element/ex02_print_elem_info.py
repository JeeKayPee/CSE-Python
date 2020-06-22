import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.selenium_utils import print_element_info


class CSETest(BaseTest1):
    def test_01(self):

        # Print element information using various inquiry methods and descriptors

        element = self.driver.find_element(By.NAME, "log")
        print_element_info("User Name Text Box", element)


if __name__ == '__main__':
    unittest.main()
