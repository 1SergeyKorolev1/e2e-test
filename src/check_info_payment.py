def check_info_payment(driver, by):
    summary_info = driver.find_element(by.CLASS_NAME, 'summary_info')
    print(f"\nИнформация о заказе / {summary_info.text}")
    return summary_info.is_displayed()