from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys


fixtures_data_count = 5


class NewVisitorTest(StaticLiveServerTestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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
        # execute browser
        self.browser.get(self.live_server_url)

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

        # start check message page
        messages_input_container = \
            self.browser.find_element_by_id('messages_input_container')

        # check messages input box
        messages_input_box = messages_input_container.find_element_by_id('msg')

        self.assertEqual(messages_input_box.get_attribute("class"),
                         "messages_input_box")

        # message send
        messages_input_box.send_keys('parkyoungwoo')
        messages_input_box.send_keys(Keys.ENTER)

        messages_list_container = \
            self.browser.find_element_by_id('messages_list_container')

        # check message element
        messages = \
            messages_list_container.find_elements_by_class_name("message")
        msg = messages[fixtures_data_count]

        msg_send_infor = \
            msg.find_element_by_class_name("message_send_information")
        msg_sender = \
            msg_send_infor.find_element_by_class_name("message_sender")
        msg_time = \
            msg_send_infor.find_element_by_class_name("message_time")
        msg_content = msg.find_element_by_class_name("message_content")

        # regex for check the time format(am/pm)
        time_regex_str = "([1]|[0-9]):[0-5][0-9](\\s)?(?i)(am|pm)"

        # check compate send message to display message
        self.assertEqual(msg_sender.text, 'bbayoung7849')
        self.assertEqual(msg_content.text, 'parkyoungwoo')
        self.assertRegex(msg_time.text, time_regex_str)
