#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

""" driver.get("https://www.amazon.com/Acer-AV15-51-7617-i7-1195G7-Graphics-Materials/dp/B09R63Z5L7/ref=sr_1_6?qid=1683130193&rnid=16225007011&s=computers-intl-ship&sr=1-6")

price = driver.find_elements(By.CLASS_NAME, "a-price-whole")

for i in price:
    print(i.text) """

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")

print("search_bar:")
print(search_bar.get_attribute("placeholder"))
print()

# Find element from element
list_documentation = driver.find_element(By.ID, "documentation")
documentation_link = list_documentation.find_element(By.TAG_NAME, "a")

print("documentation_link:")
print(documentation_link.text)
print()

# Using the xpath

footer_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[5]/ul/li[6]/a')
print(footer_link.text)
print(footer_link.get_attribute("href"))

# Print a dictionary of data

event_times = driver.find_elements(By.CLASS_NAME, "event-widget time")

for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CLASS_NAME, "event-widget ul a")

for name in event_names:
  print(name.text)

events = {}

for n in range(len(event_times)):
   events[n] = {
      "time": event_times[n].text,
      "event": event_names[n].text,
   }

print(events)
