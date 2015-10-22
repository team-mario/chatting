from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import datetime


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_new_visitor(self):
        # execute browser
        self.browser.get(self.live_server_url)

        # check browser title
        self.assertIn('issue chat', self.browser.title)

        # check h1 : team name
        text_h1 = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('TeamMario', text_h1)

        # check left navigation structure : nav > div > h2, ul > li
        nav = self.browser.find_element_by_tag_name('nav')
        div = nav.find_element_by_tag_name('div')
        h2 = div.find_element_by_tag_name('h2')
        ul = div.find_element_by_tag_name('ul')

        # check nav > h2 : sorted issue title
        text_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('Favourite Issues', text_h2)

        # check the right class? (nav > div)
        self.assertIn('sorted_issue_list', div.get_attribute('class'))

        # check search input box
        self.assertEqual(self.browser.find_element_by_id('q').get_attribute('placeholder'), 'search here')

        # check search button
        self.assertEqual(self.browser.find_element_by_id('btn_search').get_attribute('value'), 'Search')
