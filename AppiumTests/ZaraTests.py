import logging
from unittest import TestCase
from appium import webdriver as mobile
from selenium import webdriver as web
from time import sleep
from AppiumTests.Globals import ZARA_URL
from selenium.webdriver.edge.service import Service

from WebPages.ZaraYouTubePage import ZaraYouTubePage
from WebPages.ZaraHomePage import ZaraHomePage
from AppPages.DialerApp import DialerAppPage
from Globals import capabilities_Pixel_7a
from AppPages.CalcApp import CalcAppPage
from AppPages.YouTubeApp import YouTubeAppPage
from WebPages.ZaraWomanPage import ZaraWomanPage
from WebPages.ZaraCartPage import ZaraCartPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.woman_page = ZaraWomanPage(self.driver)
        self.cart_page = ZaraCartPage(self.driver)
        self.youtube_page = ZaraYouTubePage(self.driver)

# ----------------------------------------------------------------------------------------------------------------------

    def test_call_to_store(self):
        """ Test that verifies the dialer app correctly places a call to the store using the phone number
        displayed on the contact us page and ends the call successfully. The test checks if the dialed number matches
        the expected phone number """
        self.dialer_app = DialerAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        self.dialer_app.get_keyboard_pad()
        self.dialer_app.click_call(phone_number)
        self.dialer_app.end_call()
        self.assertEqual(phone_number , '1599510510')

        #self.driver = mobile.Remote(appium_server_url_local, capabilities_Pixel_9)
        #self.mobile_driver = mobile.Remote(appium_server_url_local, capabilities_Pixel_9)

# ----------------------------------------------------------------------------------------------------------------------
    def test_sms_to_store(self):
        self.dialer_app = DialerAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        self.dialer_app.get_keyboard_pad()
        self.dialer_app.fill_numbers_on_screen(phone_number)
        self.dialer_app.get_send_message_element().click()
        message = 'Hi, can you check the status of my order? Order number: 123456'
        self.dialer_app.get_text_line_message_element(message)
        self.dialer_app.get_send_message_btn_element().click()

        #self.mobile_driver = mobile.Remote(appium_server_url_local, capabilities_Pixel_9)
# ----------------------------------------------------------------------------------------------------------------------

    def test_save_zara_as_contact(self):
        self.dialer_app = DialerAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        self.dialer_app.get_keyboard_pad()
        self.dialer_app.fill_numbers_on_screen(phone_number)
        self.dialer_app.create_contact().click()
        self.dialer_app.create_contact_first_name('Zara')
        self.dialer_app.save_contact().click()

# ----------------------------------------------------------------------------------------------------------------------

    def test_compare_total_price_with_calc(self):
        """ Test that verifies if the total price in the shopping cart is correctly updated after increasing the quantity
        of a product. The test uses the calculator app to compute the expected new total price
        and compares it to the updated price in the shopping cart. """

        # Navigate through the website to add a product to the cart and open the shopping cart page.
        self.calc_app = CalcAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.woman_page.get_woman_page().click()
        self.woman_page.get_cords_category()
        self.woman_page.get_add_to_cart_element()[0].click()
        self.woman_page.get_size_element()[0].click()
        self.woman_page.get_whole_page().click()
        self.woman_page.get_shopping_cart_page()

        # Hold the old total price before modifying the quantity of the product
        old_price = self.cart_page.get_total_price()
        logging.info(f"Old Price: {old_price}")

        # Hold the old total price before modifying the quantity of the product.
        self.cart_page.get_increase_product_quantity_element()

        # Wait until the total price is updated after increasing the product quantity.
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.cart_page.get_total_price() != old_price)

        # Hold the new total price after the quantity update.
        new_price = self.cart_page.get_total_price()
        logging.info(f"New Price: {new_price}")

        # Use the calculator app to calculate the expected price (old price * 2).
        for i in str(old_price):
            self.calc_app.calc_send_keys(i)
        self.calc_app.multiple_by_2()

        # Compare the calculated price with the new price from the shopping cart.
        self.assertEqual(new_price , float(self.calc_app.get_result()))

# ----------------------------------------------------------------------------------------------------------------------

    def test_go_to_zara_youtube_channel(self):
        self.youtube_app = YouTubeAppPage(self.driver)
        # Get the current window handle (original tab)
        original_window = self.driver.current_window_handle
        self.home_page.get_youtube_page_element()
        # Wait for a new tab to open
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Switch to the new tab
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        # Now get the new URL
        print("New Tab URL:", self.driver.current_url)
        print(self.youtube_page.get_youtube_header_element())

        self.youtube_app.get_denied_notifications().click()
        self.youtube_app.get_youtube_search_element().click()
        self.youtube_app.get_youtube_edit_text_element(self.youtube_page.get_youtube_header_element())
        self.youtube_app.press_enter_element()
        self.youtube_app.get_zara_element().click()
        print(self.youtube_app.get_zara_with_strudel_element())












    def tearDown(self):
        """Clean up after the test."""
        sleep(2)
        self.driver.quit()