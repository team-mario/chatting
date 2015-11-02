__author__ = 'judelee'
from functional_tests.base import FunctionalTest


class LimitAccessTest(FunctionalTest):

    def test_limit_access_in_main_page(self):
        # The user access to main page (/accounts/profile/) without login.
        self.browser.get(self.live_server_url + '/accounts/profile')
        # The anonymous user is redirected to login page.
        self.browser.find_element_by_id('registration_btn')
