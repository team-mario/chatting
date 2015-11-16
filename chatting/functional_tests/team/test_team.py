from functional_tests.base import FunctionalTest


class TeamTest(FunctionalTest):
    fixtures = ['users.json', 'message_data.json', 'team_list.json', 'issue_data.json']

    def select_team(self):
        self.browser.find_element_by_id('btn_select_team').click()
        self.browser.find_element_by_id('element').click()

        div = self.browser.find_element_by_id('default_view')
        self.assertIn('default page', div.text)

        url_regex_str = '/issue/'

        self.assertRegex(self.browser.current_url, url_regex_str)

    def test_team(self):
        self.base_login()
        self.create_team()
        self.add_issue()
        self.select_team()

    def test_invite_user(self):
        self.base_login()
        self.create_team()
        self.browser.find_element_by_id('btn_invite').click()
        self.browser.find_element_by_id('btn_my_teams').click()
        self.browser.find_element_by_id('TestTeam').click()
        self.browser.find_element_by_id('btn_add_users').click()
        self.browser.find_element_by_id('tester2').click()
        self.browser.find_element_by_id('btn_invite_submit').click()

        self.timeout(3)
