#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')
print('udemy login')

input_name = driver.find_element(By.XPATH, '//*[@id="form-group--1"]')
input_name.clear()
input_name.send_keys('ralexrivero@gmail.com')

time.sleep(5)




driver.get("https://comidoc.net/")
driver.set_window_size(1280, 600)
print('0')

links = driver.find_elements(By.CLASS_NAME, "w-\[307px\] > a:nth-child(2)")
print('1')

link = links[0].get_attribute("href")
print('2')

driver.get(link)
print('3')

button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/article/div[3]/div/div/div[2]/div/button')
print('4')

button.click()
print('5')
# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])
print('6')
# Get the URL of the new tab
new_tab_url = driver.current_url
print(new_tab_url)
print('7')
try:
  enroll = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[5]/div/button/span')
  enroll.click()
  print('try 8')

  login = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/div/div[3]/span/a')
  print('try 9')
  login.click()
  print('try 10')

  login_page = driver.current_url
  print('try 11')

except Exception as e:
  print("something broken")

"""

  login_name = driver.find_element(By.XPATH, '//*[@id="form-group--1"]')
  login_pass = driver.find_element(By.XPATH, '//*[@id="form-group--3"]')
  login_btn = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/form/button')

  login_name.text = 'ralexrivero@gmail.com'
  login_pass.text = 'NXS79wb81py'
  login_btn.click()
# final step

check_cart = driver.current_url

final_button = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/div/aside/div/div/div[2]/div[2]/button')

final_button.click()
 """
