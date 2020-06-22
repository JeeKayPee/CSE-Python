import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.selenium_utils import print_element_info


class CSETest(BaseTest1):

    # Identify User Name field by Name
    def test_01(self):
        user_name_txt_field = self.driver.find_element(By.NAME, "log")
        print_element_info("Username Text Box", user_name_txt_field)

    # Identify User Name field by ID
    def test_02(self):
        user_name_txt_field = self.driver.find_element(By.ID, "user_login")
        print_element_info("Username Text Box", user_name_txt_field)

    #   Identify User Name field by Tag Name
    def test_03(self):
        user_name_txt_field = self.driver.find_element(By.TAG_NAME, "input")
        print_element_info("Username Text Box", user_name_txt_field)

    #   Identify User Name field by Class Name
    def test_04(self):
        user_name_txt_field = self.driver.find_element(By.CLASS_NAME, "input")
        print_element_info("Username Text Box", user_name_txt_field)

    #   Identify Submit button by Class Name (using one class from multiple classes)

    def test_05(self):
        submit_button = self.driver.find_element(By.CLASS_NAME, "input")
        print_element_info("Username Text Box", submit_button)


if __name__ == '__main__':
    unittest.main()
