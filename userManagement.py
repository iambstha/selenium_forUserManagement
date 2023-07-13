from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import re


opt = Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(5)

getUrl = input("Enter the url: ")

driver.get(getUrl)

print(driver.current_url)
print(driver.title)

try:
    username_field = driver.find_element(by=By.XPATH, value="//input[@name='username']")
    if username_field:
        print("Username field found.")
except NoSuchElementException:
    print("Username field not found.")

try:
    email_field = driver.find_element(by=By.XPATH, value="//input[@type='email']")
    if email_field:
        print("Email field found.")
except NoSuchElementException:
    print("Email field not found.")

try:
    submit_button = driver.find_element(by=By.XPATH, value="//input[@type='submit']")
    if submit_button:
        print("Submit button found.")
except NoSuchElementException:
    print("Submit button not found.")

def askInfo():
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    if validate_email(email):
        action(username,email)
    else:
        print("Action error.")

def action(username, email):
    username_field.send_keys(username)
    email_field.send_keys(email)
    try:
        if submit_button:
            submit_button.click()
            print("Added user succesfully.")
        else:
            print("No submit button found.")
    finally:
        driver.close()

def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  