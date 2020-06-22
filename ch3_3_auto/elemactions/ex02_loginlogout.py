import time
import unittest

from selenium.webdriver.common.by import By

from common.config import Configuration


class CSETest(unittest.TestCase):
    def test_something(self):
        self.driver = Configuration.create_chrome_driver()
        self.driver.get(Configuration.ADMIN_URL)
        time.sleep(3)

        user_textbox = self.driver.find_element(By.NAME, "log")
        user_textbox.send_keys(Configuration.USER_NAME)
        pwd_textbox = self.driver.find_element(By.NAME, "pwd")
        pwd_textbox.send_keys(Configuration.PASSWORD)
        pwd_textbox.submit()
        time.sleep(3)

        dboard_loaded = self.driver.find_element(By.ID, "wpadminbar").is_displayed()
        self.assertTrue(dboard_loaded, "Assert that dashboard is loaded")

        # LogOut
        logout_link = self.driver.find_element(By.XPATH, "//*[text()='Log Out']")
        self.driver.get(logout_link.get_attribute("href"))
        time.sleep(1)
        logout_msg = self.driver.find_element(By.XPATH, "//*[contains(text(),'logged out')]")
        self.assertTrue(logout_msg.is_displayed(), "Assert successful logout")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
