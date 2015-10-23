from django.test import TestCase
from django.core.urlresolvers import resolve
from message.views import list
from django.http import HttpRequest
from django.template.loader import render_to_string


#  Create your tests here.
class TeamTest(TestCase):
    # check  '/messages/issue'(url) is return right function(func : list)
    def test_issue_url_resolves_to_list(self):
        found = resolve('/messages/project-plan')
        self.assertEqual(found.func, list)

    # check that 'function list in message' is return list.html
    def test_message_list_returns_correct_html(self):
        request = HttpRequest()
        response = list(request)
        expected_html = render_to_string('message/list.html')
        self.assertEqual(response.content.decode(), expected_html)
