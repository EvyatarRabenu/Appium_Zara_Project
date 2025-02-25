import logging
from selenium import webdriver as web
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class ZaraCartPage:
    def __init__(self , driver : web.Edge):
        self.driver = driver

    def get_increase_product_quantity_element(self):
        increase_button = self.driver.find_element(By.CSS_SELECTOR, ".zds-quantity-selector__increase")
        self.driver.execute_script("arguments[0].click();", increase_button)

    def get_total_price(self):
        total_price = self.driver.find_element(By.CSS_SELECTOR , '.shop-cart-item-pricing__current>div>span').text.strip()
        total_price = ''.join(char for char in total_price if char.isdigit() or char == '.')
        price = float(total_price)
        return price

