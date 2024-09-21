from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def app():
    driver = webdriver.Chrome()
    chrome_options = Options()
    driver.get("https://www.saucedemo.com/")
    user_name_input = driver.find_element(By.ID, "user-name")
    user_name_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    add_sauce_labs_backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_sauce_labs_backpack.click()
    shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_link.click()
    cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
    if cart_item:
        print("товар добавлен в корзину")
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("standard_user")
    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("standard_user_last")
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("123456")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    summary_info = driver.find_element(By.CLASS_NAME, 'summary_info')
    print(summary_info.text)
    finish = driver.find_element(By.ID, "finish")
    finish.click()
    back_to_products = driver.find_element(By.ID, "back-to-products")
    back_to_products.click()
    print("\nсценарий тестирования завершен!")






if __name__ == "__main__":
    app()