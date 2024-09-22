from selenium import webdriver
from selenium.webdriver.common.by import By

from src.give_authorization import give_authorization
from src.added_to_cart import added_to_cart
from src.go_to_cart import go_to_cart
from src.check_product_in_cart import check_product_in_cart
from src.submission_form import giv_submission_form
from src.finish_and_back_to import finish_and_back_to

driver = webdriver.Chrome()
by = By

start_dict = {
    "link": "https://www.saucedemo.com/",
    "user_name": "standard_user",
    "password": "secret_sauce"
}
