from functional_tests.base import FunctionalTest
import time


class IssueTest(FunctionalTest):
    def test_can_move_to_own_issue_in_list(self):
        self.base_login()
        self.base_create_issues()

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issues')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        li_list = ul_list.find_element_by_tag_name('li')

        time.sleep(1)
        li_list.click()
