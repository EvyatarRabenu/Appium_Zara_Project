import logging
from unittest import TestCase
from appium import webdriver as mobile
from selenium import webdriver as web
from time import sleep
from AppiumTests.Globals import ZARA_URL, ZARA_PHONE_NUMBER, ZARA_NAME, SEARCH_ZARA_FROM_YOUTUBE, ZARA_MESSAGE
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

        # Initialize the dialer app page and navigate through the home page to find the contact information
        self.dialer_app = DialerAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()

        # Retrieve the phone number from the "Contact Us" page
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        # Initiate the call by accessing the dialer app, inputting the phone number, and making the call
        self.dialer_app.click_keyboard_pad()
        self.dialer_app.click_call(phone_number)

        # End the call after placing it
        self.dialer_app.end_call()

        # Validate that the dialed phone number matches the expected one
        self.assertEqual(phone_number , ZARA_PHONE_NUMBER)

# ----------------------------------------------------------------------------------------------------------------------

    def test_sms_to_store(self):
        """ Tests sending an SMS to the Zara store by retrieving the phone number, sending a message,
        and verifying the phone number. """

        # Initialize the dialer app page and navigate through the home page to find the contact information
        self.dialer_app = DialerAppPage(self.driver)
        self.home_page.get_hamburger_menu().click()
        self.home_page.get_info_from_hamburger()
        self.home_page.get_contact_us_element()

        # Retrieve the phone number from the "Contact Us" page
        phone_number = self.home_page.get_phone_number_element()
        logging.info(f"Zara Phone number: {phone_number}")

        # Send an SMS message to the retrieved phone number
        self.dialer_app.click_keyboard_pad()
        self.dialer_app.fill_numbers_on_screen(phone_number)
        self.dialer_app.get_send_message_element().click()
        self.dialer_app.get_text_line_message_element(ZARA_MESSAGE)
        self.dialer_app.get_send_message_btn_element().click()

        # Validate that the phone number matches the expected one
        self.assertEqual(phone_number , ZARA_PHONE_NUMBER)

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

        # Increases the product quantity
        self.cart_page.get_increase_product_quantity_element()

        # Wait until the total price is updated after increasing the product quantity.
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.cart_page.get_total_price() != old_price)

        # Hold the new total price after the quantity update.
        new_price = self.cart_page.get_total_price()
        logging.info(f"New Price: {new_price}")

        # Use the calculator app to calculate the expected price (old price * 2).
        for i in str(old_price):
            self.calc_app.calc_press_keys(i)
        self.calc_app.multiple_by_2()

        # Compare the calculated price with the new price from the shopping cart.
        self.assertEqual(new_price , float(self.calc_app.get_result()))

# ----------------------------------------------------------------------------------------------------------------------

    def test_go_to_zara_youtube_channel(self):
        """ Tests navigating to the Zara YouTube channel , opening the YouTube page in a new tab,
        switching to the new tab, denying notifications, searching for the Zara channel,
        and verifying that the search result matches the expected channel name. """

        # Initialize the YouTube app page and get the current window handle (original tab)
        self.youtube_app = YouTubeAppPage(self.driver)
        original_window = self.driver.current_window_handle

        # Navigate to the YouTube page and wait for a new tab to open
        self.home_page.get_youtube_page_element()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        # Switch to the new tab
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        # Log the new URL and the YouTube page header element
        logging.info(f"New Tab URL: {self.driver.current_url}")
        logging.info(self.youtube_page.get_youtube_header_element())

        # Deny notifications, search for the Zara channel, and press Enter to search
        self.youtube_app.get_denied_notifications().click()
        self.youtube_app.get_youtube_search_element().click()
        self.youtube_app.get_youtube_edit_text_element(self.youtube_page.get_youtube_header_element())
        self.youtube_app.press_enter_element()

        # Verify the search result matches the expected channel name
        self.assertEqual(self.youtube_page.get_youtube_header_element() , SEARCH_ZARA_FROM_YOUTUBE)


    def tearDown(self):
        """Clean up after the test."""
        sleep(2)
        self.driver.quit()