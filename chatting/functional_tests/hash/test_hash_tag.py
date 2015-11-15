from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class HashTagTest(FunctionalTest):

    def test_can_save_hash_tag_in_message(self):
        self.base_login()

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
        self.wait_for_element_with_id('id_tag_name')
        tag_name = self.browser.find_element_by_id('id_tag_name')
        tag_name.send_keys('Test_Hash_1')

        # If user add hash tag then hash tag is created at the message view.
        btn_hash_tag_submit = self.browser.find_element_by_id('btn_hash_tag_submit')
        btn_hash_tag_submit.click()

        message_hash_container = self.browser.find_element_by_id('message_hash_container')
        hash_content = message_hash_container.find_element_by_class_name('message_hash_tag_name')
        self.assertEqual(hash_content.text, '#Test_Hash_1')

    def test_can_save_hash_tag_as_message_input(self):
        self.base_login()

        div = self.browser.find_element_by_class_name('sorted_issues')
        issue_channels = div.find_elements_by_tag_name('a')
        issue_1 = issue_channels[0]
        issue_1.click()
        message_input_container = \
            self.browser.find_element_by_id('message_input_container')

        # check messages input box
        message_input_box = message_input_container.find_element_by_id('msg')

        # If the user send message like #Hash then the hash tag is saved and showed as message
        #  also with message_hash_container.
        message_input_box.send_keys('#Hash_Tag_1 LOL')
        message_input_box.send_keys(Keys.ENTER)

        import time
        time.sleep(3)
        messages_container = self.browser.find_element_by_id('messages_container')
        messages = messages_container.find_elements_by_class_name("message")

        msg = messages[-1]
        msg_content = msg.find_element_by_class_name("message_content")
        self.assertEqual(msg_content.text, '#Hash_Tag_1 LOL')

        message_hash_container = self.browser.find_element_by_id('message_hash_container')
        hash_content = message_hash_container.find_element_by_class_name('message_hash_tag_name')
        self.assertEqual(hash_content.text, '#Hash_Tag_1')
