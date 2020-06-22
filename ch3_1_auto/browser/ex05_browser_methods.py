
import time

from common.config import Configuration

driver = Configuration.create_chrome_driver()
time.sleep(3)
driver.maximize_window()
driver.get(Configuration.BLOG_URL)
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)

print("Current Window Handle: " + driver.current_window_handle)

for handle in driver.window_handles:
    print("Handle: " + handle)

driver.quit()
