#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

article_count = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div[2]/p/b/a')

# print(article_count.text)

# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Otros proyectos")
all_portals.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
