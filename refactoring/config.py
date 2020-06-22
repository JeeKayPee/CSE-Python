import logging
import os
import time
from enum import Enum, auto

from selenium import webdriver

from refactoring.os_utils import *
from settings import root_dir

LOGGER = logging.getLogger("CSE")


class Browser(Enum):
    CHROME = auto()
    FIREFOX = auto()
    HTMLUNIT = auto()


class Configuration:
    __ROOT_DIR = root_dir
    __DRIVER_DIR = os.path.join(__ROOT_DIR, "drivers")

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join(__DRIVER_DIR, "chromedriver"))
    __GECKO_DRIVER_PATH = modify_name_for_windows(os.path.join(__DRIVER_DIR, "geckodriver"))

    IP = "http://localhost:8080"  # "http://192.168.56.101";
    BLOG_URL = IP + "/"
    ADMIN_URL = IP + "/wp-admin"

    USER_NAME = "user"
    PASSWORD = "bitnami"
    MAX_WAIT_TIME = 10

    __FILES_DIR = os.path.join(__ROOT_DIR, "files")
    __SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")

    @classmethod
    def create_chrome_driver(cls):
        return webdriver.Chrome(executable_path=cls.__CHROME_DRIVER_PATH)

    @classmethod
    def create_firefox_driver(cls):
        return webdriver.Firefox(executable_path=cls.__GECKO_DRIVER_PATH)

    @classmethod
    def get_upload_file_path(cls, file_name):
        return os.path.join(cls.__FILES_DIR, file_name)

    @classmethod
    def get_screenshot_file_path(cls, file_name):
        nfile_name = "{}-{}".format(int(time.time()), file_name)
        return os.path.join(cls.__SCREENSHOTS_DIR, nfile_name)
