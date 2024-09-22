def back_to(driver, by):
    back_to_products_btn = driver.find_element(by.ID, "back-to-products")
    print("\nУспешное возвращение в магазин...")
    return back_to_products_btn.is_displayed(), back_to_products_btn.click()
