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


class RoomModelTest(TestCase):
    def test_saving_and_retrieving_message(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        room_name = 'Test'
        RoomChannel.objects.create(room_name=room_name)
        user_q = User.objects.get(username=user)
        user_q.current_room = room_name

        issue_channel = IssueChannel(channel_name="Test", channel_content="Test")
        user = User.objects.get(username=user)
        issue_channel.user = user
        issue_channel.save()

        room_q = RoomChannel.objects.get(room_name=room_name)
        room_q.issue_id_id = issue_channel.id

        room_list = room_q.issue_list
        issue_id = str(issue_channel.id)
        result_room = room_list + " " + issue_id
        room_q.issue_list = result_room
        room_q.save()

        saved_rooms = RoomChannel.objects.all()
        saved_issue_channel = IssueChannel.objects.all()

        self.assertEqual(saved_rooms.count(), 1)
        self.assertEqual(saved_rooms[0].room_name, 'Test')
        self.assertEqual(saved_issue_channel[0].channel_name, 'Test')
        self.assertEqual(saved_issue_channel[0].channel_content, 'Test')
