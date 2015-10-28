__author__ = 'judelee'
from django.test import TestCase
from team.models import IssueChannel, UserInfo


class IssueChannelFormTest(TestCase):

    def test_form_save_and_retrieve_issue_channel_form(self):
        user_info = UserInfo(user_id='JudeLee', user_password='bb')
        IssueChannel.objects.create(user_id=user_info, channel_name='test', channel_content='test contents')
        saved_channels = IssueChannel.objects.all()
        self.assertEqual(saved_channels.count(), 1)
