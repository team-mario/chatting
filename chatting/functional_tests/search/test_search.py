from functional_tests.base import FunctionalTest


class SearchTest(FunctionalTest):
    def test_search(self):
        self.base_login()
        self.browser.find_element_by_id('id_content').send_keys('test contents')
        self.browser.find_element_by_id('btn_search').click()

        search_1 = self.browser.find_element_by_id('login_error')
        search_2 = self.browser.find_element_by_id('design')
        self.assertEqual(search_1.text, 'login_error')
        self.assertEqual(search_2.text, 'design')

        search_1.click()

        url_regex_str = '/issue/.+'
        self.assertRegex(self.browser.current_url, url_regex_str)
