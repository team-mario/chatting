__author__ = 'judelee'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from base import FunctionalTest
import time


class PostIssueTest(FunctionalTest):

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def wait_for_element_with_class(self, element_class):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_class_name(element_class)
        )

    def test_can_post_issue(self):
        # User can see the "Add Issue" button in main page.
        self.browser.get(self.server_url)

        self.wait_for_element_with_id('btn_post_issue')

        self.browser.find_element_by_id('btn_post_issue').click()
        time.sleep(2)

        # If user click the button then modal is pop up.

        self.wait_for_element_with_class('modal-header')

        h4 = self.browser.find_element_by_class_name('modal-title')
        self.assertIn('Create', h4.text)

        # When issue channel's title and contents is filled user can submit through button.
        self.browser.find_element_by_id(
            'id_channel_name'
        ).send_keys('Test Issue')
        self.browser.find_element_by_id(
            'id_channel_content'
        ).send_keys('test contents')

        # After click the submit button, the user moves to new created channel.
