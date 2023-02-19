from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    browser = "c:/Users/yaro/Desktop/MyFirstFramework/chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.browser)
        )

    def close(self):
        self.driver.close()
