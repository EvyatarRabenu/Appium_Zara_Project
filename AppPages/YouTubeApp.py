from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_7a,APP_YOUTUBE
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

appium_server_url_local = 'http://localhost:4723/wd/hub'

class YouTubeAppPage:
    def __init__(self, driver):
        """Initialize the CallerApp on Pixel9 with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_7a, **APP_YOUTUBE}
        self.driver = mobile.Remote(appium_server_url_local,capabilities)

    def get_youtube_search_element(self):
        """ Returns the YouTube search element """
        return self.driver.find_element(By.XPATH , '//android.view.ViewGroup[@content-desc="Search YouTube"]')

    def get_youtube_edit_text_element(self , text):
        """ Enters the provided text into the YouTube search input field """
        edit_text = self.driver.find_element(By.ID ,'com.google.android.youtube:id/search_edit_text')
        edit_text.send_keys(text)

    def get_denied_notifications(self):
        """ Returns the element for denying notifications """
        return self.driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button")

    def press_enter_element(self):
        """ Sends the "Enter" key to the device """
        self.driver.press_keycode(66)  # KEYCODE_ENTER






