import logging
from selenium import webdriver as web
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class ZaraWomanPage:
    def __init__(self , driver : web.Edge):
        self.driver = driver

    def get_woman_page(self):
        """" Returns the link element to the women's page """
        return self.driver.find_element(By.XPATH , '//a[contains(@href, "en/woman-mkt1000")]')

    def get_cords_category(self):
        """ Clicks the "CO-ORD SETS" category link after scrolling it into view """
        wait = WebDriverWait(self.driver, 10)
        co_ords_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[contains(text(), 'CO-ORD SETS')]]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", co_ords_element)
        sleep(1)
        co_ords_element.click()

    def get_cord_name_element(self):
        """ Returns the name of the first "CO-ORD SET" product """
        cord_name_element = self.driver.find_element(By.XPATH , '//a[h2[contains(text(), "CROPPED JACKET WITH SIDE STRIPES")]]')
        cord_name = cord_name_element.text
        return cord_name

    def get_cord_price_element(self):
        """ Returns the price of the first "CO-ORD SET" product """
        cord_price_element = self.driver.find_element(By.XPATH , '(//ul[@class="product-grid-block-dynamic__row"]//li[1]//span[@class="money-amount__main"])[1]')
        cord_price = cord_price_element.text
        return cord_price

    def get_add_to_cart_element(self):
        """ Returns a list of "Add to Cart" buttons for products """
        plus_element = self.driver.find_elements(By.CSS_SELECTOR , '[data-qa-action="product-grid-open-size-selector"]')
        return plus_element


    def get_size_element(self):
        """ Returns a list of available size elements for the product """
        size_element = self.driver.find_elements(By.CSS_SELECTOR , 'div.size-selector-sizes-size__label.size-selector-sizes-size__element')
        return size_element


    def get_whole_page(self):
        """ Returns the whole page element """
        return self.driver.find_element(By.CSS_SELECTOR, '.zds-theme--light')

    def get_shopping_cart_page(self):
        """ Clicks the shopping cart icon to open the shopping cart page """
        cart_button = self.driver.find_element(By.CSS_SELECTOR, "a.layout-header-action-shop-cart")
        self.driver.execute_script("arguments[0].click();", cart_button)





