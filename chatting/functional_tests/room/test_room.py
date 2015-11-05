from functional_tests.base import FunctionalTest

fixtures_data_count = 5


class RoomTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def create_room(self):
        self.login()
        self.browser.find_element_by_id('btn_create_room').click()
        self.browser.find_element_by_id('id_team_name').send_keys('TestRoom')
        self.browser.find_element_by_id('btn_room_submit').click()

        self.timeout(2)

    def add_issue(self):
        self.create_room()
        self.browser.find_element_by_id('btn_post_issue').click()
        self.browser.find_element_by_id('id_channel_name').send_keys('Test')
        self.browser.find_element_by_id('id_channel_content').send_keys('Test')
        self.browser.find_element_by_id('btn_post_submit').click()

        self.timeout(2)

    def select_room(self):
        self.browser.find_element_by_id('room_btn').click()
        self.browser.find_element_by_id('element').click()

        div = self.browser.find_element_by_id('default_view')
        self.assertIn('default page', div.text)

        url_regex_str = '/issue/channel/'

        self.assertRegex(self.browser.current_url, url_regex_str)

    def test_select_room(self):
        self.add_issue()
        self.select_room()
