import src, checkTitle, checkTable

try:
    userManagement = src.driver.find_element(by=src.By.XPATH, value="//div[@id='user-management']")
    userManagement.click()

except src.NoSuchElementException:
    print("User management option not found")


checkTitle.checkTitle("User Management")
checkTable.checkTable()