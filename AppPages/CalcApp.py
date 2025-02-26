from appium import webdriver as mobile
from AppiumTests.Globals import capabilities_Pixel_7a,APP_CALC
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

appium_server_url_local = 'http://localhost:4723/wd/hub'


class CalcAppPage:
    def __init__(self, driver):
        """Initialize the CallerApp on Pixel9 with a WebDriver instance."""
        capabilities = {**capabilities_Pixel_7a, **APP_CALC}
        self.driver = mobile.Remote(appium_server_url_local,capabilities)
        #self.driver = driver  # השתמש במופע driver שנמסר

    def calc_press_keys(self , num):
        """ Presses the corresponding calculator key based on the given number """

        num_0 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_0')
        num_1 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_1')
        num_2 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_2')
        num_3 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_3')
        num_4 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_4')
        num_5 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_5')
        num_6 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_6')
        num_7 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_7')
        num_8 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_8')
        num_9 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_9')
        dec_point = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/dec_point')

        if num == '0':
            num_0.click()

        if num == '1':
            num_1.click()

        if num == '2':
            num_2.click()

        if num == '3':
            num_3.click()

        if num == '4':
            num_4.click()

        if num == '5':
            num_5.click()

        if num == '6':
            num_6.click()

        if num == '7':
            num_7.click()

        if num == '8':
            num_8.click()

        if num == '9':
            num_9.click()

        if num == '.':
            dec_point.click()


    def multiple_by_2(self):
        """ Multiplies the current number by 2 """
        multiple = self.driver.find_element(by=AppiumBy.ID , value='com.google.android.calculator:id/op_mul')
        sleep(1)
        multiple.click()

        digit2 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_2')
        sleep(1)
        digit2.click()


    def get_result(self):
        """ Retrieves and returns the current result displayed on the calculator """
        result_nemu = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.calculator:id/result_preview')
        return result_nemu.text








