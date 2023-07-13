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

fname_xpath = "//input[@name='fname']"
lname_xpath = "//input[@name='lname']"
email_xpath = "//input[@type='email']"
status_xpath = "//select[@id='select']"
submit_xpath = "//input[@type='submit']"


getUrl = input("Enter the url: ")

driver.get(getUrl)

try:
    submit_button = driver.find_element(by=By.XPATH, value=submit_xpath)
    if submit_button:
        print("Submit button found.")
except NoSuchElementException:
    print('Submit button not found.')

try:
    fname_field = driver.find_element(by=By.XPATH, value=fname_xpath)
    if fname_field:
        print("First name input field found.")
except NoSuchElementException:
    print('First name input field not found.')

try:
    lname_field = driver.find_element(by=By.XPATH, value=lname_xpath)
    if lname_field:
        print("Last name input field found.")
except NoSuchElementException:
    print('Last name input field not found.')

try:
    email_field = driver.find_element(by=By.XPATH, value=email_xpath)
    if email_field:
        print("Email input field found.")
except NoSuchElementException:
    print('Email input field not found.')

try:
    status_field = driver.find_element(by=By.XPATH, value=status_xpath)
    status = Select(status_field)
    if status:
        print("Status field found.")
except NoSuchElementException:
    print('Status field not found.')

def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False

def askInfo():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email= input("Enter your email address: ")
    i= input("Enter status number: ")
    fname_field.send_keys(fname)
    lname_field.send_keys(lname)
    email_field.send_keys(email)
    status.select_by_index(str(int(i) - 1))
    status_select = status.first_selected_option
    fname_value = fname_field.get_attribute('value')
    lname_value = lname_field.get_attribute('value')
    email_value = email_field.get_attribute('value')
    status_value = status_select.text

    action(fname_value,lname_value,email_value,status_value)

def action(fname_value,lname_value,email_value,status_value):
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
            print(fname_value,lname_value,email_value,status_value)
        else:
            print("Incorrect email address format.")
    try:
        driver.save_screenshot("picture.png")
        submit_button.click()
        print("Submit button clicked!")
        driver.close()
    except:
        print("Some error. ")
    driver.quit()

askInfo()
