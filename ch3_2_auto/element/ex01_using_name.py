import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1


class CSETest(BaseTest1):
    def test_01(self):
        # Identify UserName text field using By Name

        element = self.driver.find_element(By.NAME, "log")
        print(element)


if __name__ == '__main__':
    unittest.main()
