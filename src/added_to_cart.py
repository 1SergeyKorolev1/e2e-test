def added_to_cart(driver, by):
    add_sauce_labs_backpack = driver.find_element(by.ID, "add-to-cart-sauce-labs-backpack")
    add_sauce_labs_backpack.click()
    shopping_cart_link = driver.find_element(by.CLASS_NAME, "shopping_cart_link")
    shopping_cart_link.click()
    cart_item = driver.find_element(by.CLASS_NAME, "cart_item")
    if cart_item:
        print("\nТовар добавлен в корзину...")