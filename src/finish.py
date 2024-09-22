def finish(driver, by):
    finish_ = driver.find_element(by.ID, "finish")
    print("\nУспешный финиш заказа...")
    return finish_.is_displayed(), finish_.click()