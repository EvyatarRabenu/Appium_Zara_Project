from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_7a,APP_DIALER
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

appium_server_url_local = 'http://localhost:4723/wd/hub'


class DialerAppPage:
    def __init__(self, driver):
        """Initialize the CallerApp on Pixel9 with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_7a, **APP_DIALER}
        self.driver = mobile.Remote(appium_server_url_local,capabilities)
        #self.driver = driver  # השתמש במופע driver שנמסר

    def get_keyboard_pad(self):
        pad = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_fab')
        pad.click()

    def click_call(self, phone_number):
        dial_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/digits'))
        )
        dial_input.send_keys(phone_number)

        call = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_voice_call_button')
        call.click()

    def end_call(self):
        end_call_dialer = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/incall_end_call')))
        end_call_dialer.click()

    def fill_numbers_on_screen(self, phone_number):
        dial_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/digits'))
        )
        dial_input.send_keys(phone_number)

    def get_send_message_element(self):
        return self.driver.find_element(By.XPATH , '//android.widget.TextView[@resource-id="com.google.android.dialer:id/search_action_text" and @text="Send a message"]')

    def get_text_line_message_element(self , message):
        write_msg = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, 'com.google.android.apps.messaging:id/compose_message_text'))
        )
        write_msg.send_keys(message)

    def get_send_message_btn_element(self):
        return self.driver.find_element(By.ID ,'com.google.android.apps.messaging:id/send_message_button_icon')

    def create_contact(self):
        return self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/search_action_text" and @text="Create new contact"]')

    def create_contact_first_name(self , contact_name):
        first_name = self.driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.EditText[@text="First name"]')
        sleep(2)
        first_name.send_keys(contact_name)

    def save_contact(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/save_button")











