from django.test import TestCase
from login.views import index 
from django.core.urlresolvers import resolve

class LoginTest(TestCase):
    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
