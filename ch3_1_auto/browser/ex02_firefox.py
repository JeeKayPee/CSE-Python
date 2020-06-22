import os
import time

from selenium import webdriver

from settings import root_dir

# root_dir is picked up from settings.py
gecko_driver_path = os.path.join(root_dir, "drivers", "geckodriver")

driver = webdriver.Firefox(executable_path=gecko_driver_path)
time.sleep(3)
driver.quit()
