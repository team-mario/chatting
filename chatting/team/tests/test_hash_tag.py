__author__ = 'judelee'
from django.test import TestCase
from team.models import Issue, HashTag, Team
from django.contrib.auth.models import User


class HashTagTest(TestCase):

    def test_hash_tags_can_saved_into_multiple_channels(self):
        # Many to many relationships.
        hash_1 = HashTag(tag_name='soma06')
        hash_2 = HashTag(tag_name='team-mario')
        hash_3 = HashTag(tag_name='mac')

        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        team = Team.objects.create(team_name='test')

        issue_1 = Issue.objects.create(user=user, issue_name='issue_1', team=team)
        issue_2 = Issue.objects.create(user=user, issue_name='issue_2', team=team)
        issue_3 = Issue.objects.create(user=user, issue_name='issue_3', team=team)
        hash_1.save()
        hash_2.save()
        hash_3.save()
        hash_1.issues.add(issue_1)
        hash_1.issues.add(issue_2, issue_3)
        hash_2.issues.add(issue_2)
        hash_3.issues.add(issue_3)

        self.assertEqual(
            list(hash_1.issues.all()),
            [issue_1, issue_2, issue_3]
        )
        self.assertEqual(
            list(hash_2.issues.all()),
            [issue_2]
        )
        self.assertNotEqual(
            list(hash_2.issues.all()),
            [issue_3]
        )
        self.assertEqual(
            list(hash_3.issues.all()),
            [issue_3]
        )
