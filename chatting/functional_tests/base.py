from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

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

    def login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('registration_btn').click()
        self.browser.find_element_by_id('id_username').send_keys('test')
        self.browser.find_element_by_id('id_email').send_keys('test@naver.com')
        self.browser.find_element_by_id('id_password1').send_keys('test')
        self.browser.find_element_by_id('id_password2').send_keys('test')
        self.browser.find_element_by_id('registration_btn').submit()

        self.browser.find_element_by_id('id_username').send_keys('test')
        self.browser.find_element_by_id('id_password').send_keys('test')
        self.browser.find_element_by_id('login_btn').submit()

    def make_issue_channel(self, issue_name):
        self.wait_for_element_with_id('btn_post_issue')

        self.browser.find_element_by_id('btn_post_issue').click()
        time.sleep(2)

        # If user click the button then modal is pop up.

        self.wait_for_element_with_class('modal-header')

        h4 = self.browser.find_element_by_id('issue_title')
        self.assertIn('Create', h4.text)

        # When issue channel's title and contents is
        # filled user can submit through button.
        self.browser.find_element_by_id(
            'id_channel_name'
        ).send_keys(issue_name)

        self.browser.find_element_by_id(
            'id_channel_content'
        ).send_keys('test contents')

        self.browser.find_element_by_id('btn_post_submit').click()

    def post_issue_channel(self):
        self.login()

        self.make_issue_channel("Test-Issue-01")
        self.make_issue_channel("Test-Issue-02")
