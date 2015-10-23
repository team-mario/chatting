from django.test import TestCase
from django.core.urlresolvers import resolve
from message.views import list
from message.models import Message
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

class MessageModelTest(TestCase):
    def test_saving_and_retrieving_message(self):
        Message.objects.create(
            sender='bbayoung7849',
            datetime='2015-06-09 00:00:00',
            content='우하하하하하',
        )
        Message.objects.create(
            sender='mario',
            datetime='2014-06-09 00:00:00',
            content='wow',
        )

        saved_messages = Message.objects.all()

        self.assertEqual(saved_messages.count(), 2)
        self.assertEqual(saved_messages[0].sender, 'bbayoung7849')
        self.assertEqual(saved_messages[0].content, '우하하하하하')
        self.assertEqual(saved_messages[1].sender, 'mario')
        self.assertEqual(saved_messages[1].content, 'wow')
