from functional_tests.base import FunctionalTest


class TeamTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def create_team(self):
        self.browser.find_element_by_id('btn_create_team').click()
        self.browser.find_element_by_id('id_team_name').send_keys('TestTeam')
        self.browser.find_element_by_id('btn_team_submit').click()

        self.timeout(2)

    def add_issue(self):
        self.browser.find_element_by_id('btn_create_issue').click()
        self.browser.find_element_by_id('id_issue_name').send_keys('Test')
        self.browser.find_element_by_id('id_issue_content').send_keys('Test')
        self.browser.find_element_by_id('btn_post_submit').click()

        self.timeout(2)

    def select_team(self):
        self.browser.find_element_by_id('btn_select_team').click()
        self.browser.find_element_by_id('element').click()

        div = self.browser.find_element_by_id('default_view')
        self.assertIn('default page', div.text)

        url_regex_str = '/issue/'

        self.assertRegex(self.browser.current_url, url_regex_str)

    def test_select_team(self):
        self.login()
        self.create_team()
        self.add_issue()
        self.select_team()
