import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from common.config import Configuration


class CSETest(unittest.TestCase):
    def test(self):
        self.driver = Configuration.create_chrome_driver()
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.get(Configuration.ADMIN_URL)

        # Login
        user_textbox = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "log")))
        user_textbox.send_keys(Configuration.USER_NAME)
        self.assertEqual(Configuration.USER_NAME, user_textbox.get_attribute("value"), "Assert the user name text")

        pwd_textbox = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "pwd")))
        pwd_textbox.send_keys(Configuration.PASSWORD)
        self.assertEqual(Configuration.PASSWORD, pwd_textbox.get_attribute("value"), "Assert the password text")

        submit_button = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "wp-submit")))
        submit_button.click()

        self.wait.until(expected_conditions.presence_of_element_located, "//*[text()= 'WordPress Events and News']")

        # Logout
        logout_link = self.driver.find_element(By.XPATH, "//*[text()='Log Out']")
        self.driver.get(logout_link.get_attribute("href"))

        self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(text(), 'logged out')]")))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
