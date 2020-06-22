import unittest

from selenium.webdriver.common.by import By

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test(self):
        # Get cookies and print cookie information
        for cookie in self.driver.get_cookies():
            # cookie is a python dictionary
            print("Cookie information")
            print("Full text: ", cookie)
            print("Name: ", cookie['name'])
            print("Value: ", cookie['value'])
            print("Domain: ", cookie['domain'])
            print("Path: ", cookie['path'])
            print("Secure? : ", cookie['secure'])
            print("HTTPOnly? : ", cookie['httpOnly'])

            self.driver.delete_all_cookies()

            # Refresh page - Login Page should appear as session is logged out
            self.driver.refresh()
            self.driver.find_element(By.NAME, "log")

            # As we are on the home page, the tearDown in BaseTest should fail - ignore it


if __name__ == '__main__':
    unittest.main()
