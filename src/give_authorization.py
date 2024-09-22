def give_authorization(driver, by, src):
    driver.get(src.start_dict["link"])
    user_name_input = driver.find_element(by.ID, "user-name")
    user_name_input.send_keys(src.start_dict["user_name"])
    password_input = driver.find_element(by.ID, "password")
    password_input.send_keys(src.start_dict["password"])
    login_button = driver.find_element(by.ID, "login-button")
    print("Авторизация прошла успешно...")
    return [
        user_name_input.is_displayed(),
        password_input.is_displayed(),
        login_button.is_displayed(),
        login_button.click()
    ]