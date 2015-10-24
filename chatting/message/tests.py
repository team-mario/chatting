from django.test import TestCase
from django.core.urlresolvers import resolve
from message.views import message_list, message_create, message_receive
from message.models import Message
from django.http import HttpRequest
from django.template.loader import render_to_string
import json
import datetime
import time


#  Create your tests here.
class TeamTest(TestCase):
    # check  '/messages/issue'(url) is return 'message_list' function
    def test_issue_url_resolves_to_message_list(self):
        found = resolve('/messages/project-plan')
        self.assertEqual(found.func, message_list)

    # check 'message_list' function
    def test_message_list_correct_return_data(self):
        Message.objects.create(
            sender='bbayoung7849',
            datetime='2015-06-09 00:00:00',
            content='우하하하하하',
        )

        response = self.client.get('/messages/project-plan')
        messages = response.context['messages']

        # check correct json data
        for data in messages:
            self.assertEqual(data['sender'], 'bbayoung7849')
            self.assertEqual(data['content'], '우하하하하하')
            self.assertIsNotNone(data['datetime'])


    def test_message_create_from_POST_data(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sender'] = 'bbayoung7849'
        request.POST['content'] = 'wow wow'

        response = message_create(request)

        # compare stored message data to request data
        self.assertEqual(Message.objects.count(), 1)
        new_message = Message.objects.first()
        self.assertEqual(new_message.sender, 'bbayoung7849')
        self.assertEqual(new_message.content, 'wow wow')

    # 'messaage_receive' is function name
    def test_message_receive_return_correct_json_data(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sender'] = 'tester'
        request.POST['content'] = 'test contest'
        response = message_create(request)

        request = HttpRequest()
        request.method = 'GET'
        request.GET['last_primary_key'] = 10

        response = message_receive(request)
        messages = json.loads(response.content.decode())

        for data in messages:
            self.assertEqual(data['sender'], 'tester')
            self.assertEqual(data['content'], 'test contest')
            self.assertIsNotNone(data['datetime'])


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
