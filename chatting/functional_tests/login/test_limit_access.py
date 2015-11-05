__author__ = 'judelee'
from functional_tests.base import FunctionalTest


class LimitAccessTest(FunctionalTest):

    def test_limit_access_in_main_page(self):
        self.browser.get(self.live_server_url + '/issue/')
        # The anonymous user is redirected to login page.
        self.browser.find_element_by_id('btn_registration')
