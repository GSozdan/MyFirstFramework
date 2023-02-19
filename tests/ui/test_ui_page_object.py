from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #object page creation
    sign_in_page = SignInPage()

    #go to the http://github.com/login web page
    sign_in_page.go_to()

    #try to log in to GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #check that the name of the page is as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #close browser
    sign_in_page.close()
