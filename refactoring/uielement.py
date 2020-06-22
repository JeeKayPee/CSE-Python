class UiElement:
	def __init__(self, automator, element):
		self.__automator = None
		self.__element = None
		self.automator = automator
		self.element = element

	@property
	def automator(self):
		return self.__automator

	@automator.setter
	def automator(self, automator_instance):
		self.__automator = automator_instance

	@property
	def element(self):
		return self.__element

	@element.setter
	def element(self, element_instance):
		self.__element = element_instance

	def enter_text(self, text):
		self.element.send_keys(text)
		assert text, self.element.get_attribute("value")

	def submit(self, by):
		self.element.submit()
		self.automator.assert_present(by)

	def get_link(self):
		return self.element.get_attribute("href")