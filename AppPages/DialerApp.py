from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_9,APP_DIALER
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

appium_server_url_local = 'http://localhost:4723/wd/hub'


class DialerAppPage:
    def __init__(self, driver):
        """Initialize the CallerApp on Pixel9 with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_9, **APP_DIALER}
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

    def click_end_call(self):
        end_call =         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.google.android.dialer:id/incall_end_call')))
        end_call.click()
        end_call.click()

