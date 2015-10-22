from django.test import TestCase
from django.core.urlresolvers import resolve
from team.views import index
from django.http import HttpRequest
from django.template.loader import render_to_string


#  Create your tests here.
class TeamTest(TestCase):
    # root url이 index 함수를 호출하는게 맞는지 검사
    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    # index 함수가 index.html을 랜더링 하는지 검사
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('base.html')
        self.assertEqual(response.content.decode(), expected_html)
