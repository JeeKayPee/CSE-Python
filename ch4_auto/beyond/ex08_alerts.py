import unittest

from selenium.webdriver.support import expected_conditions

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test_(self):
        self.driver.execute_script("alert('Hello CSE')")

        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.dismiss()


if __name__ == '__main__':
    unittest.main()
