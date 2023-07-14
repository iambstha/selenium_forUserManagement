# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select
# import random
# import re
# from func import sample
# opt = Options()
# opt.add_argument("--headless")

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
# driver.implicitly_wait(2)

# getUrl = input("Enter the url: ")
# driver.get(getUrl)

import src, checkTitle

try:
    userManagement = src.driver.find_element(by=src.By.XPATH, value="//div[@id='user-management']")
    userManagement.click()

except src.NoSuchElementException:
    print("User management option not found")


checkTitle.checkTitleFunc("User Management")