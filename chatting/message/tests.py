from django.test import TestCase
from django.core.urlresolvers import resolve
from message.views import list, message
from message.models import Message
from django.http import HttpRequest
from django.template.loader import render_to_string
import json
import datetime

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

    # check 'list function' is return json data
    def test_func_list(self):
        Message.objects.create(
            sender='bbayoung7849',
            datetime='2015-06-09 00:00:00',
            content='우하하하하하',
        )
        response = self.client.get('/messages/project-plan')

        # get return value
        messages = response.context['messages']
        current_datetime = response.context['current_datetime']

        # check correct json data
        for data in messages:
            self.assertEqual(data['sender'], 'bbayoung7849')
            self.assertEqual(data['content'], '우하하하하하')
            self.assertIsNotNone(data['datetime'])

        # check current datetime
        self.assertIsNotNone(current_datetime)


    # check message insert from post request
    # and message return correct json data
    def test_func_message_POST_and_GET(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sender'] = 'bbayoung7849'
        request.POST['content'] = 'wow wow'

        response = message(request)

        # compare stored message data to request data
        self.assertEqual(Message.objects.count(), 1)
        new_message = Message.objects.first()
        self.assertEqual(new_message.sender, 'bbayoung7849')
        self.assertEqual(new_message.content, 'wow wow')

        # check response data
        self.assertEqual(response.content.decode(), 'inserted')

        # check return correct json data
        request = HttpRequest()
        request.method = 'GET'
        request.GET['last_update_time'] = '0'

        response = message(request)

        messages = json.loads(response.content.decode())

        for data in messages:
            self.assertIsNotNone(data['sender'])
            self.assertIsNotNone(data['datetime'])
            self.assertIsNotNone(data['content'])


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
