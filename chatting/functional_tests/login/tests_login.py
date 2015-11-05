from functional_tests.base import FunctionalTest

fixtures_data_count = 5


class LoginTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def test_logout(self):
        self.login()
        self.browser.find_element_by_id('information_btn').click()
        self.browser.find_element_by_id('id_logout').click()
        self.timeout(1)

    def test_change_password(self):
        self.login()
        self.browser.find_element_by_id('information_btn').click()
        self.browser.find_element_by_id('id_change_password').click()

        self.browser.find_element_by_id('id_old_password').send_keys('test')
        self.browser.find_element_by_id('id_new_password1').send_keys('test1')
        self.browser.find_element_by_id('id_new_password2').send_keys('test1')
        self.browser.find_element_by_id('change_password_btn').click()
        self.timeout(1)
