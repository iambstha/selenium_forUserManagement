import src

def checkTable():
    try:
        table = src.driver.find_elements(by=src.By.TAG_NAME, value="table")
        if len(table) > 0:
            print("Table is available.")
        else:
            print("Table is not available.")
    except src.NoSuchElementException:
        print("No table element found.")

    try:
        tableData = src.driver.find_elements(by=src.By.TAG_NAME, value="td")
        if len(tableData) > 0:
            print("Table data is available.")
        else:
            print("Table data is not available.")
    except src.NoSuchElementException:
        print("No table data element found.")

    try:
        editTableData = src.driver.find_elements(by=src.By.CLASS_NAME, value="editData")
        if len(editTableData) != 0:
            print("Edit option is available in table data.")
        else:
            print("Edit option is not available in table data.")
    except src.NoSuchElementException:
        print("Edit table element in the table is not found.")

    try:
        filter = src.driver.find_element(by=src.By.ID, value="filterData")
        if filter:
            print("Filter option is available.")
        else:
            print("Filter option is not available.")
    except src.NoSuchElementException:
        print("No filter option element found.")

    try:
        searchField = src.driver.find_element(by=src.By.XPATH, value="//input[@type='search']")
        if searchField:
            print("Search field found.")
    except src.NoSuchElementException:
        print("Search field not found.")

    try:
        searchButton = src.driver.find_element(by=src.By.XPATH, value="//input[@type='submit']")
        if searchButton:
            print("Search button found.")
    except src.NoSuchElementException:
        print("Search element not found.")

    try:
        resetFilter = src.driver.find_element(by=src.By.XPATH, value="//input[@id='resetFilter']")
        if resetFilter:
            print("Reset filter found.")
    except src.NoSuchElementException:
        print("Reset filter not found.")