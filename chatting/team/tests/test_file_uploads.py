__author__ = 'judelee'
from django.test import TestCase
from django.conf import settings
from team.models import Issue, AttachedFile, Team
from django.contrib.auth.models import User


class FileUploadTest(TestCase):

    def test_can_upload_file_and_retrieve(self):
        # Save file into media
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')
        team = Team.objects.create(team_name='test')
        Issue.objects.create(user=user, issue_name='test', issue_content='test contents', team=team)

        file_name = 'Test_1'
        file = 'Test_File_1'
        issue = Issue.objects.get(issue_name='test')

        created_file = AttachedFile(file_name=file_name, file=file, user=user, issue=issue)
        created_file.save()

        # Check if created file is exists in /media/issue_files directory.
        created_path = created_file.file.path
        expected_path = settings.MEDIA_ROOT + '/Test_File_1'

        self.assertEqual(created_path, expected_path)
