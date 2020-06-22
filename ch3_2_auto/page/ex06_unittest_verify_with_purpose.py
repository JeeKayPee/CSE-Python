import time
import unittest

from common.config import Configuration


class CSETest(unittest.TestCase):

    def test(self):
        driver = Configuration.create_chrome_driver()
        driver.get(Configuration.BLOG_URL)
        time.sleep(3)
        expected_title = "dummy"
        actual_title = driver.title
        self.assertEqual(actual_title, expected_title, "Check Site Title")


if __name__ == '__main__':
    unittest.main()
