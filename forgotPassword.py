from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(5)

getUrl = input("Enter the url: ")

driver.get(getUrl)

try:
    email_field = driver.find_element(by=By.XPATH, value="//input[@type='email']")
    if email_field:
        print("Email input field found.")
except NoSuchElementException:
    print(' Email input field not found.')

try:
    # submit_button = driver.find_element(by=By.XPATH, value="//input[@name='submit']")    
    submit_button = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div/form/button")
    if submit_button:
        print("Submit button found.")
except NoSuchElementException:
    print('Submit button not found.')


def askInfo():
    email = input("Enter the registered email: ")
    action(email)

def action(email):
    try:
        if email:
            email_field.send_keys(email)
    except:
        print("Email not found.")
    
    try:
        if submit_button:
            submit_button.click()
            print("Submit button clicked.")
    except:
        print("Some error.")
askInfo()