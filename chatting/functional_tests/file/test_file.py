from functional_tests.base import FunctionalTest
import os


class FileTest(FunctionalTest):

    def test_can_save_file_in_message(self):
        self.base_login()

        self.create_team()
        self.add_issue()
        div = self.browser.find_element_by_class_name('sorted_issues')
        issue_channels = div.find_elements_by_tag_name('a')
        issue_1 = issue_channels[0]
        issue_1.click()

        # User can check + Button in message view and if the user click + button, file upload button is showed
        message_input_container = \
            self.browser.find_element_by_id('message_input_container')
        plus_btn = message_input_container.find_element_by_id('btn_plus')
        self.assertEqual(plus_btn.get_attribute("class"), "message_input_plus")
        plus_btn.click()

        file_upload_btn = self.browser.find_element_by_id('item_upload_file')
        file_upload_btn.click()

        # When file upload button is clicked, the form is showed.
        self.wait_for_element_with_id('id_file_name')
        self.browser.execute_script("document.getElementById('id_file_name').style.visibility = 'visible' ")
        self.browser.execute_script("document.getElementById('id_file_name').click() ")
        file_name = self.browser.find_element_by_id('id_file_name')
        file_name.send_keys('Test_File_Upload')

        file_select_btn = self.browser.find_element_by_id('id_file')
        file_select_btn.send_keys(os.getcwd() + '/test_file')

        # If submit button the file is uploaded into message.
        btn_file_submit = self.browser.find_element_by_id('btn_file_submit')
        btn_file_submit.click()
