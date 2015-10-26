from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from team.views import index


class TeamTest(TestCase):
    # check  '/'(url) is return right function(func : index)
    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    # check that 'function index' is return base.html
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
<<<<<<< HEAD:chatting/team/tests/tests.py
        expected_html = render_to_string('issue/post_issue_form.html')
=======
        expected_html = render_to_string('common/base.html')
>>>>>>> 7af1c2c13bdd1b4a8a8c16b9c9863ab6fd7ce47f:chatting/team/tests.py
        self.assertEqual(response.content.decode(), expected_html)
