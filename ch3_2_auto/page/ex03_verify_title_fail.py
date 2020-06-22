import time
from common.config import Configuration

driver = Configuration.create_chrome_driver()
driver.get(Configuration.BLOG_URL)
time.sleep(3)
expected_title = "dummy"
actual_title = driver.title

if expected_title != actual_title:
    raise Exception(
        "Failure: Title does not match. Expected:  <{}>  Actual: <{}>   "
        .format(expected_title, actual_title)

    )

driver.quit()
