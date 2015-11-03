from django.test import TestCase
from message.views import message_list, message_create, message_receive
from django.core.urlresolvers import resolve
from message.models import Message
from team.models import IssueChannel
from django.http import HttpRequest
from django.contrib.auth.models import User
import json


#  Create your tests here.
fixtures_data_count = 5


class MessageTest(TestCase):
    fixtures = ['message_data.json', ]

    # check  '/messages/issue'(url) is return 'message_list' function
    def test_issue_url_resolves_to_message_list(self):
        found = resolve('/issue/channel/')
        self.assertEqual(found.func, message_list)

    # check 'message_list' function
    def test_message_list_return_correct_data(self):
        Message.objects.create(
            sender='mario',
            content='우하하하하하',
        )

        response = self.client.get('/issue/channel/')
        messages = response.context['messages']
        last_primary_key = response.context['last_primary_key']
        last_send_date = response.context['last_send_date']

        # regex for check the time format (am/pm)
        time_regex_str = "([1]|[0-9]):[0-5][0-9](\\s)?(?i)(am|pm)"

        last_message = messages[fixtures_data_count]
        self.assertEqual(last_message['sender'], 'mario')
        self.assertEqual(last_message['content'], '우하하하하하')
        self.assertRegex(last_message['time'], time_regex_str)

        messages_list = Message.objects.all().order_by('id')

        self.assertEqual(last_primary_key,
                         messages_list[len(messages_list) - 1].id)

        self.assertEqual(last_send_date,
                         messages_list[0].create_datetime)

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

        time_regex_str = "([1]|[0-9]):[0-5][0-9](\\s)?(?i)(am|pm)"

        for data in messages:
            self.assertTrue(data['id'] > 0)
            self.assertEqual(data['sender'], 'tester')
            self.assertEqual(data['content'], 'test contest')
            self.assertRegex(data['time'], time_regex_str)


class MessageModelTest(TestCase):
    def test_saving_and_retrieving_message_with_issue(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        issue_1 = IssueChannel.objects.create(
            user=user,
            channel_name='Issue01',
            channel_content='issue01'
        )
        issue_2 = IssueChannel.objects.create(
            user=user,
            channel_name='Issue02',
            channel_content='issue02'
        )

        Message.objects.create(
            issue=issue_1,
            sender='bbayoung7849',
            content='우하하하하하',
        )
        Message.objects.create(
            issue=issue_1,
            sender='mario',
            content='wow',
        )
        Message.objects.create(
            issue=issue_2,
            sender='tester',
            content='what',
        )

        saved_messages_in_issue_1 = Message.objects.filter(issue=issue_1)
        saved_messages_in_issue_2 = Message.objects.filter(issue=issue_2)

        self.assertEqual(saved_messages_in_issue_1.count(), 2)
        self.assertEqual(saved_messages_in_issue_1[0].sender, 'bbayoung7849')
        self.assertEqual(saved_messages_in_issue_1[0].content, '우하하하하하')
        self.assertEqual(saved_messages_in_issue_1[1].sender, 'mario')
        self.assertEqual(saved_messages_in_issue_1[1].content, 'wow')

        self.assertEqual(saved_messages_in_issue_2.count(), 1)
        self.assertEqual(saved_messages_in_issue_2[0].sender, 'tester')
        self.assertEqual(saved_messages_in_issue_2[0].content, 'what')
