from scweet.user import log_user_page
from selenium import webdriver
from scweet import utils
from time import sleep
import random
import json
import os
from scweet.utils import log_in
from selenium.webdriver.common.by import By
import csv
env_path = '.env'
listname_path = 'listname_of_all.csv'

users = []
with open(listname_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        users.append(row[1])
#print(users)
driver = utils.init_driver(headless=False)
log_in(driver, env_path, timeout=10)

error_list = []
for i in range(26,len(users)):
    log_user_page(users[i], driver)
    value = '[aria-label = "Follow @' + users[i] + '"]'
    print(value)
    sleep(random.uniform(10, 15))
    follow_button = driver.find_element(By.CSS_SELECTOR, value)
    if follow_button != None:
        follow_button.click()
    else:
        error_list.append(i)
        driver = utils.init_driver(headless=False)
        log_in(driver, env_path, timeout=10)

print(error_list)
#4,9,10,20,24