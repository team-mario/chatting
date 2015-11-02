from functional_tests.base import FunctionalTest
import time


class IssueTest(FunctionalTest):

    def test_can_move_to_own_channel_in_list(self):
        # If the user click the channel in list
        # he moves to own corresponded channel.
        # self.post_issue_channel()
        self.login()

        self.wait_for_element_with_id('btn_post_issue')

        self.browser.find_element_by_id('btn_post_issue').click()
        time.sleep(2)

        # If user click the button then modal is pop up.

        self.wait_for_element_with_class('modal-header')

        h4 = self.browser.find_element_by_id('issue_title')
        self.assertIn('Create', h4.text)

        # When issue channel's title and contents is
        # filled user can submit through button.
        self.browser.find_element_by_id(
            'id_channel_name'
        ).send_keys('Test Issue')

        self.browser.find_element_by_id(
            'id_channel_content'
        ).send_keys('test contents')

        self.browser.find_element_by_id('btn_post_submit').click()

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issue_list')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        li_list = ul_list.find_element_by_tag_name('li')

        time.sleep(2)
        li_list.click()
        pass
