from functional_tests.base import FunctionalTest
import time


class IssueTest(FunctionalTest):

    def test_can_move_to_own_issue_in_list(self):
        # If the user click the channel in list
        # he moves to own corresponded channel.
        self.login()
        self.create_issues()

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issues')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        li_list = ul_list.find_element_by_tag_name('li')

        time.sleep(2)
        li_list.click()
        pass

    def create_team(self):
        self.browser.find_element_by_id('btn_create_team').click()
        self.browser.find_element_by_id('id_team_name').send_keys('TestTeam')
        self.browser.find_element_by_id('btn_create_team_submit').click()

        time.sleep(2)

    def test_can_change_issue_status(self):
        self.login()
        self.create_team()
        self.create_issues()

        self.browser.find_element_by_id('btn_setting').click()
        self.browser.find_element_by_id('btn_select_issue').click()
        time.sleep(1)
        self.browser.find_element_by_class_name('Test-Issue-01').click()

        self.browser.find_element_by_id('btn_assignment').click()
        time.sleep(1)
        self.browser.find_element_by_id('Teammario').click()

        self.browser.find_element_by_id('btn_status').click()
        time.sleep(1)
        self.browser.find_element_by_id('0').click()
        self.browser.find_element_by_id('btn_change_status_submit').click()

    def test_can_show_issue_list(self):
        self.login()
        self.create_team()
        self.create_issues()

        self.browser.find_element_by_id('btn_issues').click()
        issue = self.browser.find_element_by_id('0Test-Issue-01')
        self.assertIn('Test-Issue-01', issue.text)
        self.browser.find_element_by_id('0Test-Issue-01').click()
