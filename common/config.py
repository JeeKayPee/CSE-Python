import os
import platform
import time

from selenium import webdriver

from settings import root_dir


def modify_name_for_windows(in_path):
    if platform.system().lower().startswith("win"):
        return in_path + ".exe"
    return in_path


class Configuration:
    __DRIVER_DIR = os.path.join(root_dir, "drivers")
    __FILES_DIR = os.path.join(root_dir, "files")
    __SCREEN_SHOTS = os.path.join(root_dir, "screenshots")

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join(__DRIVER_DIR, "chromedriver"))
    __GECKO_DRIVER_PATH = modify_name_for_windows(os.path.join(__DRIVER_DIR, "geckodriver"))

    IP = "http://localhost:8080"
    BLOG_URL = IP + "/"
    ADMIN_URL = BLOG_URL + "wp-admin"

    USER_NAME = "user"
    PASSWORD = "bitnami"

    @classmethod
    def get_screenshot_file_path(cls, file_name):
        new_file_name = "{}-{}.png".format(int(time.time()), file_name)
        return os.path.join(cls.__SCREEN_SHOTS, new_file_name)

    @classmethod
    def get_upload_file_path(cls, file_name):
        return os.path.join(cls.__FILES_DIR, file_name)

    @classmethod
    def create_firefox_driver(cls):
        return webdriver.Firefox(cls.__GECKO_DRIVER_PATH)

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
