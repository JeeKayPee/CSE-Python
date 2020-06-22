import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):

    def test_01(self):
        self.driver.find_element(By.LINK_TEXT, "Posts").click()
        self.driver.find_element(By.LINK_TEXT, "Add New").click()

        publish_button = self.wait.until(expected_conditions.presence_of_element_located((By.ID, "publish")))
        title = "Sample Title"
        title_box = self.driver.find_element(By.ID, "title")
        title_box.send_keys(title)
        self.assertEqual(title, title_box.get_attribute("value")), "Assert post title"

        self.driver.switch_to.frame('content_ifr')

        text = "Dummy text"
        content = self.driver.find_element(By.ID, "tinymce")
        content.send_keys(text)
        self.assertEquals(text, content.text, "Assert post content")

        # Once an iFrame is handled, switch back to default content (DOM root)
        self.driver.switch_to.default_content()

        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "sample-permalink")))
        publish_button.click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "View Post")))


if __name__ == '__main__':
    unittest.main()
