import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.config import Configuration


class CSETest(BaseTest1):
    def test(self):
        expected_user_name = Configuration.USER_NAME
        user_textbox = self.driver.find_element(By.NAME, "log")

        self.assertTrue(user_textbox.is_enabled(), "Assert that user name is enabled")
        user_textbox.send_keys(expected_user_name)
        actual_user_name = user_textbox.get_attribute("value")
        self.assertEqual(expected_user_name, actual_user_name, "Assert that user name is entered correctly")


if __name__ == '__main__':
    unittest.main()
