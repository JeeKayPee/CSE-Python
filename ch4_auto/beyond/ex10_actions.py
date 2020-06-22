import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test_(self):
        menu_bar = self.driver.find_element(By.ID, "wp-admin-bar-site-name")
        action_chains = ActionChains(self.driver)
        action_chains \
            .move_to_element(menu_bar) \
            .pause(1) \
            .click(self.driver.find_element(By.ID, "wp-admin-bar-view-site")) \
            .perform()

        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Site Admin")))


if __name__ == '__main__':
    unittest.main()
