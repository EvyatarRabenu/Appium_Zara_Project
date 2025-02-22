import logging
from unittest import TestCase
from appium import webdriver as mobile
from selenium import webdriver as web
from time import sleep
from AppiumTests.Globals import ZARA_URL
from selenium.webdriver.edge.service import Service
from WebPages.ZaraHomePage import ZaraHomePage
from AppPages.DialerApp import DialerAppPage
from Globals import capabilities_Pixel_9

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

appium_server_url_local = 'http://localhost:4723/wd/hub'

class ZaraTests(TestCase):

    def setUp(self):
        """ Set up the test environment. """
        service = Service(executable_path='path/to/edgedriver')
        self.driver = web.Edge(service=service)
        self.driver.get(ZARA_URL)
        self.driver.maximize_window()
        # Set implicit wait for elements to load
        self.driver.implicitly_wait(10)
        # Initialize page objects for various site components
        self.home_page = ZaraHomePage(self.driver)
        self.dialer_app = DialerAppPage(self.driver)


    def test_call_to_store(self):
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        self.dialer_app.get_keyboard_pad()
        self.dialer_app.click_call(phone_number)
        self.dialer_app.click_end_call()

        self.driver = mobile.Remote(appium_server_url_local, capabilities_Pixel_9)

    def tearDown(self):
        """Clean up after the test."""
        sleep(2)
        self.driver.quit()