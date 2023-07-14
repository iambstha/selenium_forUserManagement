import src

def checkTitle(title):
    try:
        if src.driver.title == title:
            print("The title is 'User Management'.")
        else:
            print("The title is not 'User Management'.")
    except:
        print('Title tag not found.')

