from django.test import TestCase

# Create your tests here.

class TestTestCase(TestCase):
    def test_test1(self):
        self.assertTrue(True,'true is true')

    def test_should_fail(self):
        self.assertTrue(True, 'false is not true')

    def test_should_fail2(self):
        self.assertTrue(True, 'false is not true')
