import src, checkTitle, checkTable

try:
    title = src.driver.find_element(by=src.By.TAG_NAME, value="title")
    print(title)
except:
    print("No title.")

try:
    userManagement = src.driver.find_element(by=src.By.XPATH, value="//a[@id='user-management']")
    if userManagement:
        userManagement.click()
        print("User management clicked.")
except src.NoSuchElementException:
    print("User management option not found")


checkTitle.checkTitle("User Management")
checkTable.checkTable()