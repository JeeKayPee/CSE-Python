import os
import time

from selenium import webdriver

from settings import root_dir

# root_dir is picked up from settings.py
chrome_driver_path = os.path.join(root_dir, "drivers", "chromedriver")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
time.sleep(3)
driver.quit()
