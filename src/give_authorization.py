def give_authorization(webdriver, by):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    user_name_input = driver.find_element(by.ID, "user-name")
    user_name_input.send_keys("standard_user")
    password_input = driver.find_element(by.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(by.ID, "login-button")
    login_button.click()
    print("Авторизация прошла успешно...")
    return driver