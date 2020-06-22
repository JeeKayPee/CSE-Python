import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test_(self):
        # Execute find and click in JavaScript
        self.driver.execute_script("document.getElementsByClassName('welcome-view-site')[0].click();")
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Site Admin")))
        self.driver.back()

        # Find in WebDriver, click in JavaScript
        view_site_link = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "welcome-view-site")))
        self.driver.execute_script("arguments[0].click()", view_site_link)
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Site Admin")))
        self.driver.back()

        # Find in JavaScript and return WebElement, then click in WebDriver
        view_site_link = self.driver.execute_script("return document.getElementsByClassName('welcome-view-site')[0]")
        view_site_link.click()
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Site Admin")))


if __name__ == '__main__':
    unittest.main()
