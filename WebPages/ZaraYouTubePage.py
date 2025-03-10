import logging
from selenium import webdriver as web
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class ZaraYouTubePage:
    def __init__(self , driver : web.Edge):
        self.driver = driver

    def get_youtube_header_element(self):
        """ Retrieves and returns the text of the YouTube page header (@zara) """
        return self.driver.find_element(By.CSS_SELECTOR ,'#page-header > yt-page-header-renderer > yt-page-header-view-model > div > div.page-header-view-model-wiz__page-header-headline > div > yt-content-metadata-view-model > div:nth-child(1)>span>span').text
