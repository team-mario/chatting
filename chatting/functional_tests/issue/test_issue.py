from functional_tests.base import FunctionalTest


class IssueTest(FunctionalTest):
    fixtures = ['users.json', 'message_data.json', 'team_list.json', 'issue_data.json']

    def create_issue(self, issue_name):
        self.wait_for_element_with_id('btn_create_issue')

        self.browser.find_element_by_id('btn_create_issue').click()
        self.timeout(1)

        # If user click the button then modal is pop up.
        self.wait_for_element_with_class('modal-header')

        h4 = self.browser.find_element_by_id('issue_title')
        self.assertIn('Create', h4.text)

        # When issue channel's title and contents is
        # filled user can submit through button.
        self.browser.find_element_by_id('id_issue_name').send_keys(issue_name)
        self.browser.find_element_by_id('id_issue_content').send_keys('content')

        self.browser.find_element_by_id('btn_create_issue_submit').click()

    def test_can_move_to_own_issue_in_list(self):
        self.base_login()
        self.create_team()
        self.add_issue()

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issues')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        issue_1 = ul_list.find_element_by_id('Test')

        issue_1.click()

        url_regex_str = '/issue/Test'
        self.assertRegex(self.browser.current_url, url_regex_str)
        self.timeout(3)

    def create_team(self):
        self.browser.find_element_by_id('btn_create_team').click()
        self.browser.find_element_by_id('id_team_name').send_keys('TestTeam')
        self.browser.find_element_by_id('btn_create_team_submit').click()

        self.timeout(2)

    def test_can_change_issue_status(self):
        self.base_login()
        self.create_team()
        self.create_issue("Test-Issue-01")

        self.browser.find_element_by_id('btn_setting').click()
        self.browser.find_element_by_id('btn_select_issue').click()
        self.timeout(1)
        self.browser.find_element_by_class_name('Test-Issue-01').click()

        self.browser.find_element_by_id('btn_assignment').click()
        self.timeout(1)
        self.browser.find_element_by_id('tester').click()

        self.browser.find_element_by_id('btn_status').click()
        self.timeout(1)
        self.browser.find_element_by_id('0').click()
        self.browser.find_element_by_id('btn_change_status_submit').click()

    def test_can_show_issue_list(self):
        self.base_login()
        self.create_team()
        self.create_issue("Test-Issue-01")

        self.browser.find_element_by_id('btn_issues').click()
        issue = self.browser.find_element_by_id('0Test-Issue-01')
        self.assertIn('Test-Issue-01', issue.text)
        self.browser.find_element_by_id('0Test-Issue-01').click()
        url_regex_str = '/issue/Test-Issue-01'
        self.assertRegex(self.browser.current_url, url_regex_str)
