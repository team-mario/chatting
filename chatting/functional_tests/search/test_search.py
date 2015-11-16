from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class SearchTest(FunctionalTest):

    def test_issue_contents_search(self):
        self.base_login()
        self.browser.find_element_by_id('id_content').send_keys('test contents')
        self.browser.find_element_by_id('btn_search').click()
        '''Below codes indicates issue names'''

        search_1 = self.browser.find_element_by_id('login_error')
        search_2 = self.browser.find_element_by_id('design')
        self.assertEqual(search_1.text, 'login_error')
        self.assertEqual(search_2.text, 'design')

        search_1.click()

        url_regex_str = '/issue/.+'
        self.assertRegex(self.browser.current_url, url_regex_str)

    def test_message_search(self):
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

        message_input_container = \
            self.browser.find_element_by_id('message_input_container')

        # check messages input box
        message_input_box = message_input_container.find_element_by_id('msg')

        # message send
        message_input_box.send_keys('parkyoungwoo')
        message_input_box.send_keys(Keys.ENTER)

        self.browser.find_element_by_id('id_content').send_keys('parkyoungwoo')
        self.browser.find_element_by_id('btn_search').click()
        '''Below codes indicates issue names'''

        search_1 = self.browser.find_element_by_id('Test')
        self.assertEqual(search_1.text, 'Test')

        search_1.click()

        url_regex_str = '/issue/.+'
        self.assertRegex(self.browser.current_url, url_regex_str)

        self.timeout(10)

    def test_hash_tags_search(self):
        self.base_login()
        self.browser.find_element_by_id('id_content').send_keys('#Hash_1')
        self.browser.find_element_by_id('btn_search').click()

        # Issue 1, 2 보여야함.
        pass
