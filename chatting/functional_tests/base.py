from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    fixtures = ['users.json', 'message_data.json', 'team_list.json', 'issue_data.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def wait_for_element_with_class(self, element_class):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_class_name(element_class)
        )

    def base_login(self):
        self.browser.find_element_by_id('btn_login').click()
        self.browser.find_element_by_id('id_username').send_keys('tester')
        self.browser.find_element_by_id('id_password').send_keys('test')
        self.browser.find_element_by_id('btn_login').submit()

    def timeout(self, time_to_sleep):
        time.sleep(time_to_sleep)
