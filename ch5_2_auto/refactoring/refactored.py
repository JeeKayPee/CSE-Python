import time
import unittest

from refactoring.basetest import BaseTest
from refactoring.findby import FindBy


class Refactored(BaseTest):
    def test_01(self):
        title = self.automator.find(FindBy.name("post_title"))
        title_text = "Sample" + str(int(time.time()))
        title.enter_text(title_text)
        content = self.automator.find(FindBy.name("content"))
        content.enter_text("Sample content")
        content.submit(FindBy.link_text(title_text))


if __name__ == "__main__":
    unittest.main()
