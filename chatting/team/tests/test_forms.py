__author__ = 'judelee'
from django.test import TestCase
from team.models import IssueChannel
from django.contrib.auth.models import User


class IssueChannelFormTest(TestCase):

    def test_form_save_and_retrieve_issue_channel_form(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')
        IssueChannel.objects.create(user=user, channel_name='test', channel_content='test contents')
        saved_channels = IssueChannel.objects.all()
        self.assertEqual(saved_channels.count(), 1)
