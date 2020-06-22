import time
import unittest

from common.config import Configuration


class BaseTest1(unittest.TestCase):

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
        self.driver.get(Configuration.ADMIN_URL)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

