#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/Acer-AV15-51-7617-i7-1195G7-Graphics-Materials/dp/B09R63Z5L7/ref=sr_1_6?qid=1683130193&rnid=16225007011&s=computers-intl-ship&sr=1-6")

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# ("a-offscreen")
print(price)
