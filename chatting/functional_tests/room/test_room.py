from functional_tests.base import FunctionalTest

fixtures_data_count = 5


class RoomTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', ]

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def test_create_room(self):
        self.login()
        self.browser.find_element_by_id('btn_create_room').click()
        self.browser.find_element_by_id('id_room_name').send_keys('TestRoom')
        self.browser.find_element_by_id('btn_room_submit').click()

        self.browser.find_element_by_id('room_btn').click()

        self.timeout(2)
