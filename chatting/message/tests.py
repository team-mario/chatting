from django.test import TestCase
from django.core.urlresolvers import resolve
from message.views import message_list, message_create, message_receive
from message.models import Message
from django.http import HttpRequest
import json


#  Create your tests here.
fixtures_data_count = 5


class TeamTest(TestCase):
    fixtures = ['initial_data.json', ]

    # check  '/messages/issue'(url) is return 'message_list' function
    def test_issue_url_resolves_to_message_list(self):
        found = resolve('/messages/project-plan')
        self.assertEqual(found.func, message_list)

    # check 'message_list' function
    def test_message_list_return_correct_data(self):
        Message.objects.create(
            sender='mario',
            content='우하하하하하',
        )

        response = self.client.get('/messages/project-plan')
        messages = response.context['messages']
        message = messages[fixtures_data_count]

        self.assertEqual(message['sender'], 'mario')
        self.assertEqual(message['content'], '우하하하하하')

        last_primary_key = Message.objects.last().id
        self.assertEqual(response.context['last_primary_key'],
                         last_primary_key)

    def test_message_create_from_POST_data(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['sender'] = 'testing_goat'
        request.POST['content'] = 'wow_wow'

        message_create(request)

        self.assertEqual(Message.objects.count(), fixtures_data_count + 1)
        new_message = Message.objects.last()
        self.assertEqual(new_message.sender, 'testing_goat')
        self.assertEqual(new_message.content, 'wow_wow')

    # check 'messaage_receive' function
    def test_message_receive_return_correct_json_data(self):
        last_primary_key = Message.objects.last().id

        request = HttpRequest()
        request.method = 'POST'
        request.POST['sender'] = 'tester'
        request.POST['content'] = 'test contest'
        message_create(request)

        request = HttpRequest()
        request.method = 'GET'
        request.GET['last_primary_key'] = last_primary_key

        response = message_receive(request)
        messages = json.loads(response.content.decode())

        for data in messages:
            self.assertTrue(data['id'] > 0)
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
