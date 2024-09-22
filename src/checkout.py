def checkout(driver, by):
    checkout_button = driver.find_element(by.ID, "checkout")
    return checkout_button.is_displayed(), checkout_button.click()