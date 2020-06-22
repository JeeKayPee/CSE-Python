import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):

    # Handling a drop down list with clicks
    def test_01(self):
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "blogname")))
        raw_drop_down = self.driver.find_element(By.ID, "start_of_week")
        raw_drop_down.click()

        expected_day = "Monday"
        locator = "//option[text()='{}']".format(expected_day)
        option = self.driver.find_element(By.XPATH, locator)
        option.click()

        self.assertTrue(option.is_selected(), "Assert Monday is selected as start of the week")

    # Handling a drop down list using send_keys
    def test_02(self):
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "blogname")))
        raw_drop_down = self.driver.find_element(By.ID, "start_of_week")
        raw_drop_down.click()

        expected_day = "Monday"
        raw_drop_down.send_keys(expected_day)

        locator = "//option[text()='{}']".format(expected_day)
        option = self.driver.find_element(By.XPATH, locator)

        self.assertTrue(option.is_selected(), "Assert Monday is selected as start of the week")

    # Handling a drop down list  as a Select Control
    def test_03(self):
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "blogname")))
        raw_drop_down = self.driver.find_element(By.ID, "start_of_week")
        raw_drop_down.click()

        expected_day = "Monday"
        week_start = Select(raw_drop_down)
        week_start.select_by_visible_text(expected_day)
        actual_day = week_start.first_selected_option.text

        self.assertEqual(expected_day, actual_day, "Verifying Selected Start of a week")


if __name__ == '__main__':
    unittest.main()
