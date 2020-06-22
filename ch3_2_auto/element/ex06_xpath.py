import unittest

from selenium.webdriver.common.by import By

from common.base_test_1 import BaseTest1
from common.selenium_utils import print_element_info


class CSETest(BaseTest1):

    # Identify User Name text field with Absolute XPath (Tag Name)
    # Don't use this in professional work. Absolute XPath are evil ;-)
    def test_00(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/form/p[1]/label/input")
        print_element_info("User Name text field", element)

    # Now onwards, we stick with relative XPath as Absolute XPath are brittle
    # Identify User Name text field with XPath - Tag Name
    def test_01(self):
        element = self.driver.find_element(By.XPATH, "//input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Tag Name and attribute name
    def test_02(self):
        element = self.driver.find_element(By.XPATH, "//input[@type]")
        print_element_info("User Name text field", element)

    # Identify Password text field with XPath - Tag Name, attribute name and attribute value
    def test_03_01(self):
        element = self.driver.find_element(By.XPATH, "//input[@type='password']")
        print_element_info("Password text field", element)

    # Identify User Name text field with XPath
    # Variant of test03_01: ID
    def test_03_02(self):
        element = self.driver.find_element(By.XPATH, "//input[@ID='user_login']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath
    # Variant of test03_01: ClassName
    def test_03_03(self):
        element = self.driver.find_element(By.XPATH, "//input[@class='input']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath
    # Variant of test03_01: name
    def test_03_04(self):
        element = self.driver.find_element(By.XPATH, "//input[@name='log']")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath
    # Variant of test03_01: name (any tag with attribute and value)
    def test_03_05(self):
        element = self.driver.find_element(By.XPATH, "//*[@name='log']")
        print_element_info("User Name text field", element)

    # Identify Lost your password link with XPath - Text
    def test_04(self):
        element = self.driver.find_element(By.XPATH, "//*[text()='Lost your password?']")
        print_element_info("Lost your password link", element)

    # Identify User Name text field with XPath - Relationships - Child
    def test_05_01(self):
        element = self.driver.find_element(By.XPATH, "//p/input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Relationships - Following Sibling
    def test_05_02(self):
        element = self.driver.find_element(By.XPATH, "//br/following-sibling::input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Partial Match - Attribute Value Contains
    def test_06_01(self):
        element = self.driver.find_element(By.XPATH, "//input[contains(@id,'er_l')]")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Partial Match - Attribute value starts with
    def test_06_02(self):
        element = self.driver.find_element(By.XPATH, "//input[starts-with(@id,'user_l')]")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Partial Match - Attribute value ends with
    # Ends with is not supported in current browsers
    # It requires XPath V2.0 while all browsers use XPath 1.0 4
    # This test will fail
    def test_06_03(self):
        element = self.driver.find_element(By.XPATH, "//input[ends-with(@id,'_login')]")
        print_element_info("User Name text field", element)

    # Identify Lost your password link with XPath - Partial Match - text contains
    def test_06_04(self):
        element = self.driver.find_element(By.XPATH, "//a[contains(text(),'Lost')]")
        print_element_info("Lost your password link", element)

    # Identify Lost your password link with XPath - Partial Match - Text Starts with
    def test_06_05(self):
        element = self.driver.find_element(By.XPATH, "//a[starts-with(text(),'Lost')]")
        print_element_info("Lost your password link", element)

    # Identify User Name text field with XPath - Logical OR : using or keyword
    def test_07_01(self):
        element = self.driver.find_element(By.XPATH, "//input[@class='input' or @id='user_pass']")
        print_element_info("User Name text field", element)

    # Identify Password text field with XPath - Logical AND : using and keyword
    def test_07_02(self):
        element = self.driver.find_element(By.XPATH, "//input[@type and @name='pwd']")
        print_element_info("Password text field", element)

    # Identify Password text field with XPath - Logical Not : using not() function
    def test_07_03(self):
        element = self.driver.find_element(By.XPATH, "//input[@type and not(@name='log')]")
        print_element_info("Password text field", element)

    # Identify Login Form with XPath - Hierarchy (Axis) - Parent
    def test_08_01(self):
        element = self.driver.find_element(By.XPATH, "//label/../..")
        print_element_info("Login Form", element)

    # Identify User Name text field with XPath - Hierarchy (Axis)
    # Descendant (using // instead of / between form and input)
    def test_08_02(self):
        element = self.driver.find_element(By.XPATH, "//form//input")
        print_element_info("User Name text field", element)

    # Identify Login Form with XPath - Hierarchy (Axis)
    # Ancestor (using /ancestor)
    def test_08_03(self):
        element = self.driver.find_element(By.XPATH, "//input/ancestor::form")
        print_element_info("Login Form", element)

    # Identify User Name text field with XPath - Hierarchy (Axis)
    # Preceding Sibling (starting from submit paragraph)
    def test_08_04(self):
        element = self.driver.find_element(By.XPATH, "//p[@class='submit']/preceding-sibling::p//input")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Index (Index uses Human Counting)
    # This variant looks at children of the same parent
    # this is the reason //input[2] does not point to the Password text field
    def test_09_01(self):
        element = self.driver.find_element(By.XPATH, "//input[1]")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Index (Index uses Human Counting)
    # This variant looks at elements across the DOM
    # this is the reason (//input[2]) would point to the Password text field
    def test_09_02(self):
        element = self.driver.find_element(By.XPATH, "(//input)[1]")
        print_element_info("User Name text field", element)

    # Identify User Name text field with XPath - Multiple attribute names
    def test_10_01(self):
        element = self.driver.find_element(By.XPATH, "//input[@type and @name]")
        print_element_info("User Name text field", element)

    # Identify Password text field with XPath - Multiple attribute names and values
    def test_10_02(self):
        element = self.driver.find_element(By.XPATH, "//input[@type='password' and @name='pwd']")
        print_element_info("Password text field", element)


if __name__ == '__main__':
    unittest.main()
