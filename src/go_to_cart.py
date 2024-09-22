def go_to_cart(driver, by):
    shopping_cart_link = driver.find_element(by.CLASS_NAME, "shopping_cart_link")
    return shopping_cart_link.is_displayed(), shopping_cart_link.click()