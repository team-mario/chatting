from functional_tests.base import FunctionalTest
import time


class IssueTest(FunctionalTest):

    def test_can_move_to_own_channel_in_list(self):
        # If the user click the channel in list
        # he moves to own corresponded channel.
        self.post_issue_channel()

        sorted_issue_list = self.browser.find_element_by_class_name('sorted_issue_list')
        ul_list = sorted_issue_list.find_element_by_tag_name('ul')
        li_list = ul_list.find_element_by_tag_name('li')

        time.sleep(2)
        li_list.click()
        pass
