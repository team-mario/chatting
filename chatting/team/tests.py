from django.test import TestCase
from django.core.urlresolvers import resolve
from team.views import index
from django.http import HttpRequest
from django.template.loader import render_to_string


#  Create your tests here.
class TeamTest(TestCase):
    # check  '/'(url) is return right function(func : index)
    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        print(found.func)
        # self.assertEqual(found.func, '')

    # check that 'function index' is return base.html
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('common/base.html')
        self.assertEqual(response.content.decode(), expected_html)
