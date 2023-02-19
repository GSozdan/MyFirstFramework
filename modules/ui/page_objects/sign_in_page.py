from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    url = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.url)

    def try_login(self, login, password):
        #find field where to fill incorrect username or email
        login_field = self.driver.find_element(By.CSS_SELECTOR, '#login_field')
        
        #fill incorrect username or email
        login_field.send_keys(login)

        #find field where to fill incorrect password
        password_field = self.driver.find_element(By.CSS_SELECTOR, '#password')

        #fill incorrect password
        password_field.send_keys(password)

        #find the sign in button
        button = self.driver.find_element(By.CSS_SELECTOR, "[name='commit']")

        #click on the button
        button.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
