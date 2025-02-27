from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_7a,APP_DIALER
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

appium_server_url_local = 'http://localhost:4723/wd/hub'

class DialerAppPage:
    def __init__(self, driver):
        """ Initialize the CallerApp on Pixel7_a with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_7a, **APP_DIALER}
        self.driver = mobile.Remote(appium_server_url_local,capabilities)


    def click_keyboard_pad(self):
        """ Opens the dialer keypad """
        pad = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_fab')
        pad.click()

    def click_call(self, phone_number):
        """ Enters a phone number and makes a call """
        dial_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/digits'))
        )
        dial_input.send_keys(phone_number)
        call = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_voice_call_button')
        call.click()

    def end_call(self):
        """ Ends the current call """
        end_call_dialer = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/incall_end_call')))
        end_call_dialer.click()

    def fill_numbers_on_screen(self, phone_number):
        """ Enters a phone number in the dialer input field """
        dial_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/digits'))
        )
        dial_input.send_keys(phone_number)

    def get_send_message_element(self):
        """ Returns the 'Send a message' button element """
        return self.driver.find_element(By.XPATH , '//android.widget.TextView[@resource-id="com.google.android.dialer:id/search_action_text" and @text="Send a message"]')

    def get_text_line_message_element(self , message):
        """ Types a message into the message input field """
        write_msg = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'com.google.android.apps.messaging:id/compose_message_text'))
        )
        write_msg.send_keys(message)

    def get_send_message_btn_element(self):
        """ Returns the send message button element """
        return self.driver.find_element(By.ID ,'com.google.android.apps.messaging:id/send_message_button_icon')












