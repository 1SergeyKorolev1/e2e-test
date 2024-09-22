def check_product_in_cart(driver, by):
    cart_item = driver.find_element(by.CLASS_NAME, "cart_item")
    if cart_item.is_displayed():
        print("\nТовар добавлен в корзину...")
    return cart_item.is_displayed()