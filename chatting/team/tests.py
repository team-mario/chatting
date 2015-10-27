from django.test import TestCase
from django.core.urlresolvers import resolve
from login.views import index


#  Create your tests here.
class TeamTest(TestCase):
    # check  '/'(url) is return right function(func : index)
    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    # check that 'function index' is return redirected url
    def test_index_returns_correct_redirected_url(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/accounts/login/')
