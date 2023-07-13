from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import re
opt = Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(2)

fname_xpath = ''
lname_xpath = ''
email_xpath = ''
status_xpath = ''
submit_xpath = ''


getUrl = input("Enter the url: ")

driver.get(getUrl)

try:
    submit_button = driver.find_element(by=By.XPATH, value="//input[@type='submit']")
    if submit_button:
        print("Submit button found.")
except NoSuchElementException:
    print('Submit button not found.')

try:
    fname_field = driver.find_element(by=By.XPATH, value="//input[@name='fname']")
    if fname_field:
        print("First name input field found.")
except NoSuchElementException:
    print('First name input field not found.')

try:
    lname_field = driver.find_element(by=By.XPATH, value="//input[@name='lname']")
    if lname_field:
        print("Last name input field found.")
except NoSuchElementException:
    print('Last name input field not found.')

try:
    email_field = driver.find_element(by=By.XPATH, value="//input[@type='email']")
    if email_field:
        print("Email input field found.")
except NoSuchElementException:
    print('Email input field not found.')

try:
    status_id = driver.find_element(by=By.ID, value="select")
    status = Select(status_id)
    if status:
        print("Status field found.")
except NoSuchElementException:
    print('Status field not found.')


def askInfo():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email= input("Enter your email address: ")
    status_options = status.options
    status_select = status.select_by_index(0)
    fname_value = fname.__getattribute__('value')
    lname_value = lname.__getattribute__('value')
    email_value = email.__getattribute__('value')
    status_value = status_select

    action(fname_value,lname_value,email_value,status_value)

def action(fname_value,lname_value,email_value,status_value):
    try:
        if fname_value == '':
            print("Empty first name.")
        if lname_value == '':
            print("Empty last name.")
        if status_value == '':
            print("Status not selected.")
        if email_value == '':
            print("Empty email address.")
        else:
            if validate_email(email_value):
                print("Email address is validated.")
            else:
                print("Incorrect email address format.")
        if submit_button:
            submit_button.click()
            driver.save_screenshot("picture.png")
            driver.close()
    except:
        print("Completed task. ")
    driver.close()



def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False 