__author__ = 'judelee'
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/judelee/Downloads/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()