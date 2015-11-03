__author__ = 'judelee'
from django.test import TestCase
from team.models import IssueChannel
from django.contrib.auth.models import User
from team.models import RoomChannel


class IssueChannelFormTest(TestCase):

    def test_form_save_and_retrieve_issue_channel_form(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')
        IssueChannel.objects.create(user=user, channel_name='test', channel_content='test contents')
        saved_channels = IssueChannel.objects.all()
        self.assertEqual(saved_channels.count(), 1)


class RoomFormTest(TestCase):
    def test_form_save_and_retrieve_issue_channel_form(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        issue_channel = IssueChannel(channel_name='test', channel_content='test contents')
        user = User.objects.get(username=user)
        issue_channel.user = user

        RoomChannel.objects.create(room_name='test room')
        room_q = RoomChannel.objects.get(room_name='test room', issue_id=issue_channel.id)
        issue_channel.save()
        room_q.save()

        saved_channels = IssueChannel.objects.all()
        saved_rooms = RoomChannel.objects.all()

        self.assertEqual(saved_channels.count(), 1)
        self.assertEqual(saved_rooms.count(), 1)
