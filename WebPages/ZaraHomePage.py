import logging
from selenium import webdriver as web
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class ZaraHomePage:
    def __init__(self , driver : web.Edge):
        self.driver = driver


    def get_home_page_element(self):
       """ Returns the home page element """
       return self.driver.find_element(By.CSS_SELECTOR,'h1>a')

    def get_hamburger_menu(self):
       """ Returns the hamburger menu button element """
       return self.driver.find_element(By.CSS_SELECTOR ,'button[data-qa-id="layout-header-toggle-menu"]')


    def get_info_from_hamburger(self):
        """ Clicks the "+ INFO" link in the hamburger menu using JavaScript """
        wait = WebDriverWait(self.driver, 10)
        info_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "+ INFO")))
        # Use JavaScript to click the element
        self.driver.execute_script("arguments[0].click();",info_element)

        # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "+ INFO")))
        # info_element = self.driver.find_element(By.LINK_TEXT , "+ INFO")
        # return info_element

    def get_contact_us_element(self):
        """ Scrolls to and clicks the "CONTACT US" link under a specific category in the menu """
        wait = WebDriverWait(self.driver, 10)
        contact_us_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-categoryid='11113']//a[.//span[text()='CONTACT US']]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", contact_us_element)
        sleep(1)
        contact_us_element.click()

    def get_phone_number_element(self):
        """ Returns the phone number displayed on the contact us page, formatted without spaces """
        phone_number_element = self.driver.find_element(By.CSS_SELECTOR,'div>.contact-item-description__phone')
        phone_number = phone_number_element.text
        phone_number = phone_number.replace(' ' , '')
        return phone_number

    def get_youtube_page_element(self):
        youtube_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//ul[@id="homeSocialFooter"]//a[contains(@href, "youtube.com/user/zara")]'))
        )

        # Click the element using JavaScript to bypass obstructions
        self.driver.execute_script("arguments[0].click();", youtube_element)






