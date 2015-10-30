from functional_tests.base import FunctionalTest


class IssueTest(FunctionalTest):

    def test_can_move_to_own_channel_in_list(self):
        # If the user click the channel in list he moves to own corresponded channel.
        self.post_issue_channel()
        pass