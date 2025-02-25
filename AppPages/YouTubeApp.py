from time import sleep

from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_7a,APP_YOUTUBE
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



appium_server_url_local = 'http://localhost:4723/wd/hub'


class YouTubeAppPage:
    def __init__(self, driver):
        """Initialize the CallerApp on Pixel9 with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_7a, **APP_YOUTUBE}
        self.driver = mobile.Remote(appium_server_url_local,capabilities)


    def get_youtube_search_element(self):
        return self.driver.find_element(By.XPATH , '//android.view.ViewGroup[@content-desc="Search YouTube"]')

    def get_youtube_edit_text_element(self , text):
        edit_text = self.driver.find_element(By.ID ,'com.google.android.youtube:id/search_edit_text')
        edit_text.send_keys(text)

    def get_denied_notifications(self):
        return self.driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button")

    # def get_zara_element(self):
    #     return self.driver.find_element(By.XPATH , '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.youtube:id/results"]/android.view.ViewGroup[3]/android.view.ViewGroup')

    def get_zara_element(self):

        # Wait until element appears
        # return WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//android.widget.Button[@content-desc="Go to channel"]')))

        sleep(5)
        return self.driver.find_element(By.XPATH , '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.youtube:id/results"]/android.view.ViewGroup[4]')

        # sleep(5)
        # return self.driver.find_element(By.XPATH , '//android.widget.ImageView[@content-desc="Go to channel"]')

    def press_enter_element(self):
        # Send the "Enter" key
        self.driver.press_keycode(66)  # KEYCODE_ENTER

    def get_zara_with_strudel_element(self):
        # sleep(5)
        # return self.driver.find_element(By.XPATH ,'//android.widget.FrameLayout[@resource-id="com.google.android.youtube:id/collapsing_header_container"]/android.view.ViewGroup/android.view.ViewGroup[3]').text

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//android.widget.ImageView[@content-desc="Go to channel"]'))

        )
        return element




