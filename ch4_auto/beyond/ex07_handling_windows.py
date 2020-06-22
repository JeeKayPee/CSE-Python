import unittest

from common.base_test_2 import BaseTest2
from common.config import Configuration


class CSETest(BaseTest2):
    def test_(self):
        print(self.driver.title)
        main_win = self.driver.current_window_handle

        # open blog URL in a new Window/Tab
        self.driver.execute_script("window.open(arguments[0]);", Configuration.BLOG_URL)

        for handle in self.driver.window_handles:
            if handle != main_win:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
                self.driver.close()

        self.driver.switch_to.window(main_win)
        print(self.driver.title)

        # Assert that the new window was closed
        self.assertEqual(len(self.driver.window_handles), 1, "Verify whether new window is closed")


if __name__ == '__main__':
    unittest.main()
