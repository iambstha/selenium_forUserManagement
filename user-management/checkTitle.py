import src

def checkTitle(title):
    wait = src.WebDriverWait(src.driver, 10)

    title_element = wait.until(src.EC.presence_of_element_located((src.By.TAG_NAME, "title")))
    actual_title = title_element.get_attribute("text")

    if actual_title == title:
        print("The title is 'User Management'.")
    else:
        print("The title is not 'User Management'.")
