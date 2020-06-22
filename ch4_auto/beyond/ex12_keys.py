import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test_01(self):
        # Sending sequence Using Keys
        title = "Sample"
        post_title = self.driver.find_element(By.NAME, "post_title")
        post_title.send_keys(Keys.SHIFT + title)
        self.assertEqual(title.upper(), post_title.get_attribute("value"), "Assert upper case title")

    def test_02(self):
        # Holding and releasing a key while other keystrokes are simulated
        title = "Sample"
        post_title = self.driver.find_element(By.NAME, "post_title")
        action_chain = ActionChains(self.driver)
        action_chain \
            .key_down(Keys.SHIFT) \
            .send_keys_to_element(post_title, title) \
            .key_up(Keys.SHIFT) \
            .perform()

        self.assertEqual(title.upper(), post_title.get_attribute("value"), "Assert upper case title")


if __name__ == '__main__':
    unittest.main()
