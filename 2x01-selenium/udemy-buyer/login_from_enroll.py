#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



login_page = driver.get('https://www.udemy.com/join/signup-popup/?next=%2Fcart%2Fcheckout%2Fexpress%2Fcourse%2F5196632%2F%3FdiscountCode%3D921A28CFC49344909970')

time.sleep(25)

login_link = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/div/div/div/div[3]/span/a')

print(login_link.get_attribute('href'))

login_link.click()

# captcha check
time.sleep(5)

""" captcha_url = driver.current_url

captcha_check = driver.find_element(By.CSS_SELECTOR, '#challenge-stage > div > label > input[type=checkbox]')

captcha_check.click() """

time.sleep(5)

login_form = driver.current_url

print(login_form)

input_name = driver.find_element(By.XPATH, '//*[@id="form-group--1"]')
input_name.clear()
input_name.send_keys('ralexrivero@gmail.com')

time.sleep(5)
