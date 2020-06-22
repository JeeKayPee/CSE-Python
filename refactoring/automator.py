from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from refactoring.config import Browser, Configuration
from refactoring.uielement import UiElement


class WebAutomator:

    def __init__(self, browser):
        self.__driver = None
        self.__waiter = None
        if browser == Browser.CHROME:
            self.driver = Configuration.create_chrome_driver()
        elif browser == Browser.FIREFOX:
            self.driver = Configuration.create_firefox_driver()
        else:
            raise Exception("Unsupported browser: " + browser.name)
        self.waiter = WebDriverWait(self.driver, Configuration.MAX_WAIT_TIME)

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver_instance):
        self.__driver = driver_instance

    @property
    def waiter(self):
        return self.__waiter

    @waiter.setter
    def waiter(self, waiter_instance):
        self.__waiter = waiter_instance

    def __wait(self, condition):
        return UiElement(self, self.waiter.until(condition))

    def wait_until_present(self, by):
        print(by.by, by.value)
        return self.__wait(EC.presence_of_element_located((by.by, by.value)))

    def wait_until_clickable(self, by):
        return self.__wait(EC.element_to_be_clickable((by.by, by.value)))

    def find(self, by):
        return self.wait_until_present(by)

    def go_to(self, url, by):
        self.driver.get(url)
        return self.wait_until_present(by)

    def close_all(self):
        self.driver.quit()

    def assert_present(self, by):
        try :
            self.wait_until_present(by)
        except Exception as e:
            raise AssertionError("Element not present" + str(e))