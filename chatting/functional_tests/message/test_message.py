from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys


fixtures_data_count = 5


class NewVisitorTest(FunctionalTest):
    fixtures = ['initial_data.json', ]

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
