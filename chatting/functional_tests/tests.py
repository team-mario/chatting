from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def test_cannot_add_invalid_id_and_password(self):
        self.browser.get(self.server_url)
        self.get_item_input_login_box().send_keys('\n')
        alert = self.browser.switch_to_alert()
        error = alert.text
        alert.accept()

        self.assertEqual(error, 'Invalid id or password')

        self.get_item_input_password_box().send_keys('\n')
        alert = self.browser.switch_to_alert()
        error = alert.text
        alert.accept()
        self.assertEqual(error, 'Invalid id or password')

        self.get_item_input_login_box().send_keys('test id')
        self.get_item_input_password_box().send_keys('test password\n')

        alert = self.browser.switch_to_alert()
        error = alert.text
        alert.accept()
        self.assertEqual(error, 'Invalid id or password')

    def test_cannot_register_invalid_form(self):
        self.browser.get(self.server_url)

        self.browser.find_element_by_id('register_btn').click()
        self.browser.find_element_by_id('id_name').send_keys('123')
        self.browser.find_element_by_id('id_password').send_keys('321')
        self.browser.find_element_by_id('id_checkPassword').send_keys('123')
        self.browser.find_element_by_id('submit_btn').click()


class NewVisitorTest(FunctionalTest):

    def check_basic_layout(self):
        # check browser title
        self.assertIn('issue chat', self.browser.title)

        # check h1 : team name
        text_h1 = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('TeamMario', text_h1)

        # check left navi structure : #nav > .sorted_issue_list > h2, ul > li
        nav = self.browser.find_element_by_id('nav')
        div = nav.find_element_by_class_name('sorted_issue_list')
        h2 = div.find_element_by_tag_name('h2')

        # check nav > h2 : sorted issue title
        self.assertEqual('Favourite Issues', h2.text)

        # check the right class? (nav > div)
        self.assertIn('sorted_issue_list', div.get_attribute('class'))

        # check search input box
        input_search = self.browser.find_element_by_id('q')
        self.assertEqual(input_search.get_attribute('placeholder'),
                         'search here')

        # check search button
        btn_search = self.browser.find_element_by_id('btn_search')
        self.assertEqual(btn_search.get_attribute('value'), 'Search')

    def test_new_visitor(self):
        self.login()
        self.check_basic_layout()

        # find element by id 'project plan' issue
        issue_project_plan = self.browser.find_element_by_id('project-plan')

        url_regex_str = '/messages/.+'

        # check issue 'project plan' href
        self.assertRegex(issue_project_plan.get_attribute('href'),
                         url_regex_str)

        issue_project_plan.click()

        # current browser url validation width regex
        self.assertRegex(self.browser.current_url, url_regex_str)

        self.check_basic_layout()



