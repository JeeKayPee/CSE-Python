import unittest

from selenium.webdriver.common.by import By

from common.base_test_2 import BaseTest2
from common.selenium_utils import print_element_info


class CSETest(BaseTest2):
    def test(self):
        self.driver.find_element(By.LINK_TEXT, "Posts").click()
        self.driver.find_element(By.LINK_TEXT, "Categories").click()

        table = self.driver.find_element(By.CLASS_NAME, "wp-list-table")
        first_cb = table.find_element(By.NAME, "delete_tags[]")
        print_element_info("Category Check Box: ", first_cb)
        first_cb.click()

        self.assertTrue(first_cb.is_selected(), "Assert checkbox selection")


if __name__ == '__main__':
    unittest.main()
