__author__ = 'judelee'
from base import FunctionalTest
import time


class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)

        self.fail('could not find window')

    def test_login_with_persona(self):

        # JudeLee goes to the team-mario site.
        self.browser.get(self.server_url)
        self.assertIn('Team-mario', self.browser.title)

        # He notices a "Sign in " button for the first time and click.
        self.browser.find_element_by_class_name('login_btn').click()

        # The page moves to facebook login page.
        self.switch_to_new_window('Facebook')

        # He logs with facebook by clicking confirm button.
        self.browser.find_element_by_id(
            'email'
        ).send_keys('sgs4716@naver.com')
        self.browser.find_element_by_id(
            'pass'
        ).send_keys('dlehdduq01')

        self.browser.find_element_by_id('u_0_2').click()

        # The facebook page closed and can get back to Team-mario site.
        self.switch_to_new_window('Team-mario')

        # He can see that he is logged in.
