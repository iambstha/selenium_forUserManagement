from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re
opt = Options()
# opt.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(5)

getUrl = input("Enter the url: ")
driver.get(getUrl)