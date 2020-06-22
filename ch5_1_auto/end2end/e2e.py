import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from common.base_test_2 import BaseTest2


class CSETest(BaseTest2):
    def test_update_settings(self):
        self.driver.maximize_window()

        # Go to Setting
        self.driver.find_element(By.LINK_TEXT, "Settings").click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "submit")))

        # Update the blog title to Selenium Blog
        blog_title = "Selenium Blog"
        blog_name = self.driver.find_element(By.ID, "blogname")
        blog_name.clear()
        blog_name.send_keys(blog_title)
        self.assertEqual(blog_title, blog_name.get_attribute("value"), "Blog Title should {}. ".format(blog_title))

        # Update User can register
        users_can_register = self.driver.find_element(By.ID, "users_can_register")
        if not users_can_register.is_selected():
            users_can_register.click()
        self.assertTrue(users_can_register.is_selected(), "Verify that anyone can register is checked")

        # Update the date format to m/d/Y format
        target_radio = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='m/d/Y']")
        target_radio.click()
        self.assertTrue(target_radio.is_selected(),
                        "{} Date format should be selected".format(target_radio.get_attribute("value")))

        # Update Weeks Starts to Monday
        expected_week_day = "Monday"
        week_start = Select(self.driver.find_element(By.ID, "start_of_week"))
        week_start.select_by_visible_text(expected_week_day)
        actual_week_start = week_start.first_selected_option.text
        self.assertEqual(expected_week_day, actual_week_start, "Verify selected Start of week")

        self.driver.find_element(By.ID, "submit").click()
        # self.driver.find_element(By.TAG_NAME, "form").submit()
        self.assertTrue(self.driver.find_element(By.XPATH, "//strong[text()='Settings saved.']").is_displayed(),
                        "Settings should be saved")

    def test_create_preview_delete_posts(self):

        # Click Posts link, Add new
        self.driver.find_element(By.LINK_TEXT, "Posts").click()
        self.driver.find_element(By.LINK_TEXT, "Add New").click()

        title = "Sample Title"
        title_box = self.driver.find_element(By.ID, "title")
        title_box.send_keys(title)
        self.assertEqual(title, title_box.get_attribute("value")), "Assert post title"

        self.driver.switch_to.frame("content_ifr")

        text = "Dummy text"
        content = self.driver.find_element(By.ID, "tinymce")
        content.send_keys(text)
        self.assertEqual(text, content.text, "Assert post content")

        # Once an iFrame is handled, switch back to default content (DOM root)
        self.driver.switch_to.default_content()

        # Click on Publish button
        self.driver.find_element(By.ID, "publish").click()

        # get current window
        main_win = self.driver.current_window_handle

        # Click post preview button
        self.driver.find_element(By.ID, "post-preview").click()

        for handle in self.driver.window_handles:
            if handle != main_win:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
                self.driver.close()

        # Switch to main window
        self.driver.switch_to.window(main_win)

        # Assert that the new window was closed
        self.assertEqual(len(self.driver.window_handles), 1, "verify if new window is closed")
        time.sleep(5)
        # Click on Move Trash
        self.driver.find_element(By.LINK_TEXT, "Move to Trash").click()


if __name__ == '__main__':
    unittest.main()
