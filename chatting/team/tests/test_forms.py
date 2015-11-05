__author__ = 'judelee'
from django.test import TestCase
from team.models import IssueChannel, TeamChannel
from django.contrib.auth.models import User


class IssueChannelFormTest(TestCase):

    def test_form_save_and_retrieve_issue_channel_form(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        team = TeamChannel.objects.create(team_name='test')
        user = User.objects.get(username='john')
        IssueChannel.objects.create(user=user, channel_name='test', channel_content='test contents', team=team)
        saved_channels = IssueChannel.objects.all()
        self.assertEqual(saved_channels.count(), 1)


class RoomModelTest(TestCase):
    def test_saving_and_retrieving_team(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        team = TeamChannel.objects.create(team_name='Test')
        issue_1 = IssueChannel.objects.create(
            user=user,
            channel_name='Test 1',
            channel_content='Test 1',
            team=team
        )

        issue_2 = IssueChannel.objects.create(
            user=user,
            channel_name='Test 2',
            channel_content='Test 2',
            team=team
        )

        self.assertEqual(issue_1.team.team_name, 'Test')
        self.assertEqual(issue_1.channel_name, 'Test 1')
        self.assertEqual(issue_1.channel_content, 'Test 1')

        self.assertEqual(issue_2.team.team_name, 'Test')
        self.assertEqual(issue_2.channel_name, 'Test 2')
        self.assertEqual(issue_2.channel_content, 'Test 2')
