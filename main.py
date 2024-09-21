from selenium.webdriver.common.by import By
import src

def app():
    driver = src.driver
    src.give_authorization(driver, By, src)
    src.added_to_cart(driver, By)
    src.giv_submission_form(driver, By)
    src.finish_and_back_to(driver, By)
    driver.close()
    driver.quit()
    print("\nСценарий тестирования завершен!")

if __name__ == "__main__":
    app()