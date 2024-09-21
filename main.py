from selenium import webdriver
from selenium.webdriver.common.by import By
from src.give_authorization import give_authorization
from src.added_to_cart import added_to_cart
from src.submission_form import giv_submission_form
from src.finish_and_back_to import finish_and_back_to

def app():
    driver = give_authorization(webdriver, By)
    added_to_cart(driver, By)
    giv_submission_form(driver, By)
    finish_and_back_to(driver, By)
    driver.close()
    driver.quit()
    print("\nПроизведен выход с платформы...")
    print("\nСценарий тестирования завершен!")

if __name__ == "__main__":
    app()