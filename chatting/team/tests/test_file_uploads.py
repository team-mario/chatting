__author__ = 'judelee'
from django.test import TestCase
from django.conf import settings
from team.models import IssueChannel, ChannelFiles, TeamChannel
from django.contrib.auth.models import User


class FileUploadTest(TestCase):

    def test_can_upload_file_and_retrieve(self):
        # Save file into media
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        team = TeamChannel.objects.create(team_name='test')
        IssueChannel.objects.create(user=user, channel_name='test', channel_content='test contents', team=team)

        title = 'Test_1'
        file = 'Test_File_1'
        channel = IssueChannel.objects.get(channel_name='test')

        ChannelFiles.objects.create(title=title, file=file, channel=channel)

        # Check if created file is exists in /media/channel_files directory.
        created_file = ChannelFiles.objects.get(pk=1)
        created_path = created_file.file.path
        expected_path = settings.MEDIA_ROOT + '/Test_File_1'

        self.assertEqual(created_path, expected_path)
