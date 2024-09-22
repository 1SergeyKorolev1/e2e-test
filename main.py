import src

def app():
    driver = src.driver
    by = src.by
    src.give_authorization(driver, by, src)
    src.added_to_cart(driver, by)
    src.go_to_cart(driver, by)
    src.check_product_in_cart(driver, by)
    src.giv_submission_form(driver, by)
    src.finish_and_back_to(driver, by)
    driver.close()
    driver.quit()
    print("\nСценарий тестирования завершен!")

if __name__ == "__main__":
    app()