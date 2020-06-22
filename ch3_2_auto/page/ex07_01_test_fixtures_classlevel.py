import time
import unittest

from common.config import Configuration


class CSETest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):
        CSETest.driver = Configuration.create_chrome_driver()

    @classmethod
    def tearDownClass(self):
        CSETest.driver.quit


def test_pass(self):
    CSETest.driver.get(Configuration.BLOG_URL)
    time.sleep(3)
    expected_title = "CSE Blog"
    actual_title = CSETest.driver.title
    self.assertEqual(actual_title, expected_title, "Check Site Title")


def test_fail(self):
    CSETest.driver.get(Configuration.BLOG_URL)
    time.sleep(3)
    expected_title = "Dummy"
    actual_title = CSETest.driver.title
    self.assertEqual(actual_title, expected_title, "Check Site Title")


if __name__ == '__main__':
    unittest.main()
