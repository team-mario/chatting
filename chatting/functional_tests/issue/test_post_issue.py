__author__ = 'judelee'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from base import FunctionalTest


class PostissueTest(FunctionalTest):

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def test_can_post_issue(self):
        # User can see the "Add Issue" button in main page.
        self.browser.get(self.server_url)

        self.wait_for_element_with_id('btn_post_issue')

        self.browser.find_element_by_id('btn_post_issue')
        # If user click the button then modal is pop up.


        # When issue channel's title and contents is filled user can submit through button.

        # After click the submit button, the user moves to new created channel.

