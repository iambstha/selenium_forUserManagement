from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

opt = Options()
# opt.add_experimental_option("detach",True)
opt.add_argument("--headless")
# opt.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(5)

getUrl = input("Enter the login page url: ")

driver.get(getUrl)

# u_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[1]/input"
# p_xpath = "/html/body/div/div/div[2]/div[2]/div/form/div[2]/input"
# submit_xpath = "/html/body/div/div/div[2]/div[2]/div/form/button"

try:
    search_u_field = driver.find_element(by=By.XPATH, value="//input[@id='username']")
    search_p_field = driver.find_element(by=By.XPATH, value="//input[@id='password']")
    submit_field = driver.find_element(by=By.XPATH, value="//button[@name='login']")
    if search_u_field:
        print("Username field found.")
    if search_p_field:
        search_p_field_type = driver.find_element(by=By.XPATH, value="//input[@id='password'][@type='password']")
        if search_p_field_type:
            print("Password field found & is hidden.")
        else:
            print("Alert: Password is not hidden.")
    if submit_field:
        print("Submit button found.")
except:
    print("Error: Username, password or submit field not found.")

def askInfo():
    username = input("Username: ")
    password = input("Password: ")
    findComponents(username,password)

def findComponents(username,password): 

    try:
        # u_text_box = driver.find_element(by=By.XPATH, value=u_xpath)
        u_text_box = search_u_field
        if u_text_box:
            # print('Username field found.')
            u_text_box.send_keys(username)
    except NoSuchElementException:
        print('Username field not found.')

    try:
        # p_text_box = driver.find_element(by=By.XPATH, value=p_xpath)
        p_text_box = search_p_field
        if p_text_box:
            # print('Password field found.')
            p_text_box.send_keys(password)
    except NoSuchElementException:
        print('Password field not found.')

    try:
        # submit_button = driver.find_element(by=By.XPATH, value=submit_xpath)
        submit_button = submit_field
        if submit_button:
            submit_button.click()
            print('Submit clicked.')
    except NoSuchElementException:
        print('Submit button not found.')

    try:
        check_login_status = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/form/button")
        if check_login_status.text == 'Log out':
            print("Successfully logged in.") 
    except NoSuchElementException:
        print('Error: Username or password doesnot match!!!')
    
    driver.close()
    
askInfo()