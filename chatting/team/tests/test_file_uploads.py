__author__ = 'judelee'
from django.test import TestCase
from django.conf import settings
from team.models import IssueChannel, ChannelFiles
from django.contrib.auth.models import User


class FileUploadTest(TestCase):

    def test_can_upload_file_and_retrieve(self):
        # Save file into media
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')
        IssueChannel.objects.create(user=user, channel_name='test', channel_content='test contents')

        title = 'Test_1'
        channel = IssueChannel.objects.get(pk=1)
        file = 'Test_File_1'
        ChannelFiles.objects.create(title=title, file=file, channel=channel)

        # Check if created file is exists in /media/channel_files directory.
        
