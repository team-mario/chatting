from django.test import TestCase
from message.views import get_messages, create_message, get_message
from django.core.urlresolvers import resolve
from message.models import Message
from team.models import Issue
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.importlib import import_module
from team.models import Team
import json


#  Create your tests here.
fixtures_data_count = 5


class MessageTest(TestCase):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    # check  '/issue/'(url) is return 'get_messages' function
    def test_issue_url_resolves_to_message_list(self):
        found = resolve('/issue/')
        self.assertEqual(found.func, get_messages)

    # check 'get_messages' function
    def test_get_messages_return_correct_data(self):
        issue = Issue.objects.first()

        engine = import_module(settings.SESSION_ENGINE)
        session_key = None

        request = HttpRequest()
        request.method = 'GET'
        request.user = User.objects.first()
        request.session = engine.SessionStore(session_key)

        response = get_messages(request, issue.issue_name)

        messages = response.context_data['messages']
        last_primary_key = response.context_data['last_primary_key']
        last_send_date = response.context_data['last_send_date']

        # regex for check the time format (am/pm)
        time_regex_str = "([1]|[0-9]):[0-5][0-9](\\s)?(?i)(am|pm)"

        for idx, data in enumerate(Message.objects.filter(issue=issue).order_by('id')):
            message = messages[idx]
            self.assertEqual(message['content'], data.content)
            self.assertEqual(message['sender'], data.sender)
            self.assertRegex(message['time'], time_regex_str)

        messages_list = Message.objects.filter(issue=issue).order_by('id')

        self.assertEqual(last_primary_key,
                         messages_list[len(messages_list) - 1].id)

        self.assertEqual(last_send_date,
                         messages_list[0].create_datetime)

    def test_create_message_from_POST_data(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['issue_name'] = Issue.objects.first().issue_name
        request.POST['sender'] = 'testing_goat'
        request.POST['content'] = 'wow_wow'

        create_message(request)

        self.assertEqual(Message.objects.count(), fixtures_data_count + 1)
        new_message = Message.objects.last()
        self.assertEqual(new_message.sender, 'testing_goat')
        self.assertEqual(new_message.content, 'wow_wow')

    # check 'get_message' function
    def test_get_message_return_correct_json_data(self):
        last_primary_key = Message.objects.last().id

        request = HttpRequest()
        request.method = 'POST'
        request.POST['issue_name'] = Issue.objects.first().issue_name
        request.POST['sender'] = 'tester'
        request.POST['content'] = 'test contest'
        create_message(request)

        request = HttpRequest()
        request.method = 'GET'
        request.GET['last_primary_key'] = last_primary_key
        request.GET['issue_name'] = Issue.objects.first().issue_name

        response = get_message(request)
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
        team = Team.objects.create(team_name='team')
        issue_1 = Issue.objects.create(
            user=user,
            issue_name='Issue01',
            issue_content='issue01',
            team=team
        )
        issue_2 = Issue.objects.create(
            user=user,
            issue_name='Issue02',
            issue_content='issue01',
            team=team
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

        saved_message_in_issue_1 = Message.objects.filter(issue=issue_1)
        saved_message_in_issue_2 = Message.objects.filter(issue=issue_2)

        self.assertEqual(saved_message_in_issue_1.count(), 2)
        self.assertEqual(saved_message_in_issue_1[0].sender, 'bbayoung7849')
        self.assertEqual(saved_message_in_issue_1[0].content, '우하하하하하')
        self.assertEqual(saved_message_in_issue_1[1].sender, 'mario')
        self.assertEqual(saved_message_in_issue_1[1].content, 'wow')

        self.assertEqual(saved_message_in_issue_2.count(), 1)
        self.assertEqual(saved_message_in_issue_2[0].sender, 'tester')
        self.assertEqual(saved_message_in_issue_2[0].content, 'what')
