from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

opt = Options()
opt.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.maximize_window()
driver.implicitly_wait(5)

getUrl = input("Enter the login page URL: ")
driver.get(getUrl)

select_xpath = "/html/body/form/select"
select_field = driver.find_element(by=By.XPATH, value=select_xpath)

select_value = Select(select_field)


select_value.select_by_index(2)  # Select the second option


selected_option = select_value.first_selected_option
print("Selected Option:", selected_option.text)

driver.quit()
