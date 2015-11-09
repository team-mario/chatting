from functional_tests.base import FunctionalTest


class TeamTest(FunctionalTest):
    def create_team(self):
        self.browser.find_element_by_id('btn_create_team').click()
        self.browser.find_element_by_id('id_team_name').send_keys('TestTeam')
        self.browser.find_element_by_id('btn_create_team_submit').click()

        self.timeout(1)

    def add_issue(self):
        self.browser.find_element_by_id('btn_create_issue').click()
        self.browser.find_element_by_id('id_issue_name').send_keys('Test')
        self.browser.find_element_by_id('id_issue_content').send_keys('Test')
        self.browser.find_element_by_id('btn_create_issue_submit').click()

        self.timeout(1)

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
