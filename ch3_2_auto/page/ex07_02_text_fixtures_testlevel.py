import time
import unittest

from common.config import Configuration


class CSETest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__driver = None

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver_instance):
        self.__driver = driver_instance

    def setUp(self):
        self.driver = Configuration.create_chrome_driver()

    def tearDown(self):
        self.driver.quit()

    def test_pass(self):
        # CSETest.driver.get(Configuration.BLOG_URL)
        self.driver.get(Configuration.BLOG_URL)
        time.sleep(3)
        expected_title = "CSE Blog"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title, "Check Site Title")

    def test_fail(self):
        self.driver.get(Configuration.BLOG_URL)
        time.sleep(3)
        expected_title = "Dummy"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title, "Check Site Title")


if __name__ == '__main__':
    unittest.main()
