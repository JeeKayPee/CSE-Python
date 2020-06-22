import time

from common.config import Configuration

driver = Configuration.create_chrome_driver()
driver.get(Configuration.BLOG_URL)
time.sleep(3)

print("URL: " + driver.current_url)
print("Title: " + driver.title)
print("Page Source: " + driver.page_source)

driver.quit()
