from functional_tests.base import FunctionalTest


class HashTagTest(FunctionalTest):

    def test_can_save_hash_tag_in_message(self):
        # execute browser
        self.login()

        self.create_issues()
        div = self.browser.find_element_by_class_name('sorted_issues')
        issue_channels = div.find_elements_by_tag_name('a')
        issue_1 = issue_channels[0]
        issue_1.click()

        # User can check + Button in message view and if the user click + button, add hash tag button is showed
        message_input_container = \
            self.browser.find_element_by_id('message_input_container')
        plus_btn = message_input_container.find_element_by_id('btn_plus')
        self.assertEqual(plus_btn.get_attribute("class"), "message_input_plus")
        plus_btn.click()

        hash_tag_btn = self.browser.find_element_by_id('item_add_hash_tag')
        hash_tag_btn.click()

        # If the user click add hash tag button hash tag form is showed.

        # If user add hash tag then hash tag is created at the message view.

        pass