import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.selenium_utils import print_element_info


class CSETest(BaseTest1):
    # Identify user name text field with CSS Selector (Tag Name)
    def test_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input")
        print_element_info("User Name text field", element)

    # Identify user name text field with CSS Selector (Tag Name with a given attribute)
    def test_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[type]")
        print_element_info("User Name text field", element)

    # Identify Password text field with CSS Selector (Tag Name, a given attribute (Type) and attribute value)
    def test_03_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        print_element_info("Password text field", element)

    # Identify User Name text field with CSS Selector (Tag Name, a given attribute (ID) and attribute value)
    # Variant of test03
    def test_03_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id='user_login']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector (Tag Name, a given attribute(Class) and attribute value)
    # Variant of test03
    def test_03_03(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[class='input']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector (Tag Name, a given attribute(name) and attribute value)
    # Variant of test03
    def test_03_04(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='log']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Special Symbols - (# means ID)
    def test_04_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "#user_login")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Special Symbols - (. means Class)
    def test_04_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Special Symbols - (* means any tag)
    def test_04_03(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "*[name='log']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Relationship (Parent - Child). Denoted with >
    def test_05_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "p>input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Relationship (Sibling). Denoted with +
    def test_05_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "br+input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Partial Match - Contains - *=
    def test_06_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id*='er_l']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Partial Match - Start with - ^=
    def test_06_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Partial Match - Ends with - $=
    def test_06_03(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id$='login']")
        print_element_info("User Name text field", element)

    # Identify Submit button with CSS Selector
    # Partial Match - Contains Word - ~=
    def test_06_04(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[value~='In']")
        print_element_info("Log In button", element)

    # Identify User Name text field with CSS Selector
    # Logical OR (comma ,)
    def test_07_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input, *[name='log']")
        print_element_info("User name text field", element)

    # Identify User name text field with CSS Selector - Logical Operator
    # We can give a class with the . operator which acts as an OR condition on the previous part of
    # CSS Selector
    def test_07_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input.input")
        print_element_info("User Name text field", element)

    # Identify Password text field with CSS Selector - Logical Operator
    # We can give a class with the # operator which acts as an AND condition on the previous part of
    # CSS Selector
    def test_07_03(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input#user_pass")
        print_element_info("Password text field", element)

    # Identify Password text field with CSS Selector - Logical Operator - using not() function
    def test_07_04(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input:not([name='log'])")
        print_element_info("Password text field", element)

    # Identify User Name text field with CSS Selector
    # Multiple attributes (only attribute names)
    def test_08_01(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[type][name]")
        print_element_info("User Name text field", element)

    # Identify User Name text field with CSS Selector
    # Multiple attributes with values
    def test_08_02(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='log']")
        print_element_info("User name text field", element)


if __name__ == '__main__':
    unittest.main()
