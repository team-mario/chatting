from functional_tests.base import FunctionalTest


class IssueTest(FunctionalTest):
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
        self.create_issue("Test-Issue-01")
        self.create_issue("Test-Issue-02")

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issues')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        issue_1 = ul_list.find_element_by_id('Test-Issue-01')

        issue_1.click()

        url_regex_str = '/issue/Test-Issue-01'
        self.assertRegex(self.browser.current_url, url_regex_str)
