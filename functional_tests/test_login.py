__author__ = 'judelee'

from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
import time



class LoginTest(FunctionalTest):

    def test_login_with_persona(self):

        # When user enter into site he notices a "Sign in with facebook" for the firsttime
        self.browser.get(self.server_url)

        # When he clicks login btn he get into facebook.

        # After login he get to next page and can see the logout button .


