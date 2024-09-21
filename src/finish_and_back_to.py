def finish_and_back_to(driver, by):
    summary_info = driver.find_element(by.CLASS_NAME, 'summary_info')
    print(f"\nИнформация о заказе / {summary_info.text}")
    finish = driver.find_element(by.ID, "finish")
    finish.click()
    print("\nУспешный финиш заказа...")
    back_to_products = driver.find_element(by.ID, "back-to-products")
    back_to_products.click()
    print("\nУспешное возвращение в магазин...")
