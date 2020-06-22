import unittest

from refactoring.automator import WebAutomator
from refactoring.config import Configuration, Browser
from .findby import FindBy


class BaseTest(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	@property
	def automator(self):
		return self.__automator

	@automator.setter
	def automator(self, automator):
		self.__automator = automator

	def setUp(self):
		self. automator = WebAutomator(Browser.CHROME)
		user_text_box = self.automator.go_to(Configuration.ADMIN_URL, FindBy.name("log"))
		user_text_box.enter_text(Configuration.USER_NAME)
		pwd_text_box = self.automator.find(FindBy.name("pwd"))
		pwd_text_box.enter_text(Configuration.PASSWORD)
		pwd_text_box.submit(FindBy.id("wpadminbar"))
	
	def tearDown(self):
		log_out = self.automator.find(FindBy.xpath("//*[text()='Log Out']"))
		self.automator.go_to(log_out.get_link(), FindBy.xpath("//*[contains(text(),'logged out')]"))
		self.automator.close_all()
