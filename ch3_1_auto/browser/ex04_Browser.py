import time

from common.config import Configuration

driver = Configuration.create_chrome_driver()
time.sleep(3)
driver.quit()
