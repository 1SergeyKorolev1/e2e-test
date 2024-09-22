import src

def app():
    driver = src.driver
    by = src.by
    src.give_authorization(driver, by, src)
    src.added_to_cart(driver, by)
    src.go_to_cart(driver, by)
    src.check_product_in_cart(driver, by)
    src.checkout(driver, by)
    src.giv_submission_form(driver, by)
    src.check_info_payment(driver, by)
    src.finish(driver, by)
    src.back_to(driver, by)
    driver.close()
    driver.quit()
    print("\nСценарий тестирования завершен!")

if __name__ == "__main__":
    app()