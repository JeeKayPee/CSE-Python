import unittest

from common.base_test_2 import BaseTest2
from common.config import Configuration


class CSETest(BaseTest2):
    def test_(self):
        target_path = Configuration.get_screenshot_file_path("dashboard")
        self.driver.save_screenshot(target_path)


if __name__ == '__main__':
    unittest.main()
