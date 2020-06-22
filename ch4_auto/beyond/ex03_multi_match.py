import unittest

from selenium.webdriver.common.by import By

from common.base_test_2 import BaseTest2
from common.selenium_utils import print_element_info


class CSETest(BaseTest2):
    def test(self):
        self.driver.find_element(By.LINK_TEXT, "Posts").click()
        self.driver.find_element(By.LINK_TEXT, "Categories").click()

        del_check_boxes = self.driver.find_elements(By.NAME, "delete_tags[]")
        print("Check Box count: ", len(del_check_boxes))

        for check_box in del_check_boxes:
            print_element_info("Category Check Box: ", check_box)
            check_box.click()
            self.assertTrue(check_box.is_selected(), "Assert checkbox selection")


if __name__ == '__main__':
    unittest.main()
