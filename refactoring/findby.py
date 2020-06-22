from selenium.webdriver.common.by import By


class _By:

    def __init__(self, by_type, value):
        self.__by = by_type
        self.__value = value

    @property
    def by(self):
        return self.__by

    @property
    def value(self):
        return self.__value


class _ById(_By):

    def __init__(self, value):
        super().__init__(By.ID, value)


class _ByName(_By):

    def __init__(self, value):
        super().__init__(By.NAME, value)


class _ByClass(_By):

    def __init__(self, value):
        super().__init__(By.CLASS_NAME, value)


class _ByTag(_By):

    def __init__(self, value):
        super().__init__(By.TAG_NAME, value)


class _ByLinkText(_By):

    def __init__(self, value):
        super().__init__(By.LINK_TEXT, value)


class _ByPartialLinkText(_By):

    def __init__(self, value):
        super().__init__(By.PARTIAL_LINK_TEXT, value)


class _ByXPath(_By):

    def __init__(self, value):
        super().__init__(By.XPATH, value)


class _ByCssSelector(_By):

    def __init__(self, value):
        super().__init__(By.CSS_SELECTOR, value)


class FindBy:

    @classmethod
    def id(cls, value):
        return _ById(value)

    @classmethod
    def name(cls, value):
        return _ByName(value)

    @classmethod
    def class_name(cls, value):
        return _ByClass(value)

    @classmethod
    def tag_name(cls, value):
        return _ByTag(value)

    @classmethod
    def link_text(cls, value):
        return _ByLinkText(value)

    @classmethod
    def partial_link_text(cls, value):
        return _ByPartialLinkText(value)

    @classmethod
    def xpath(cls, value):
        return _ByXPath(value)

    @classmethod
    def css_selector(cls, value):
        return _ByCssSelector(value)
