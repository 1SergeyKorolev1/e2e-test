def giv_submission_form(driver, by):
    first_name_input = driver.find_element(by.ID, "first-name")
    first_name_input.send_keys("standard_user")
    last_name_input = driver.find_element(by.ID, "last-name")
    last_name_input.send_keys("standard_user_last")
    postal_code = driver.find_element(by.ID, "postal-code")
    postal_code.send_keys("123456")
    continue_button = driver.find_element(by.ID, "continue")
    print("\nФорма успешно заполнена и отправлена...")
    return [
        first_name_input.is_displayed(),
        last_name_input.is_displayed(),
        postal_code.is_displayed(),
        continue_button.is_displayed(),
        continue_button.click()
    ]