from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
        print(cls.server_url)

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_item_input_login_box(self):
        return self.browser.find_element_by_id('login-id')

    def get_item_input_password_box(self):
        return self.browser.find_element_by_id('login-password')

    def login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('register_btn').click()
        self.browser.find_element_by_id('id_name').send_keys('jang')
        self.browser.find_element_by_id('id_password').send_keys('jang')
        self.browser.find_element_by_id('id_checkPassword').send_keys('jang')

        self.browser.find_element_by_id('submit_btn').click()
        self.get_item_input_login_box().send_keys('jang')
        self.get_item_input_password_box().send_keys('jang')

        self.browser.find_element_by_id('login_btn').click()