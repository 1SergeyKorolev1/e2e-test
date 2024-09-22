def added_to_cart(driver, by):
    add_sauce_labs_backpack = driver.find_element(by.ID, "add-to-cart-sauce-labs-backpack")
    return add_sauce_labs_backpack.is_displayed(), add_sauce_labs_backpack.click()