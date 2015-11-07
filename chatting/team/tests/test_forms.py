__author__ = 'judelee'
from django.test import TestCase
from team.models import Issue, Team
from django.contrib.auth.models import User


class IssueFormTest(TestCase):

    def test_form_save_and_retrieve_issue_issue_form(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        team = Team.objects.create(team_name='test')
        user = User.objects.get(username='john')
        Issue.objects.create(user=user, issue_name='test', issue_content='test contents', team=team)
        saved_issues = Issue.objects.all()
        self.assertEqual(saved_issues.count(), 1)


class TeamModelTest(TestCase):
    def test_saving_and_retrieving_team(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        team = Team.objects.create(team_name='Test')
        issue_1 = Issue.objects.create(
            user=user,
            issue_name='Test 1',
            issue_content='Test 1',
            team=team
        )

        issue_2 = Issue.objects.create(
            user=user,
            issue_name='Test 2',
            issue_content='Test 2',
            team=team
        )

        self.assertEqual(issue_1.team.team_name, 'Test')
        self.assertEqual(issue_1.issue_name, 'Test 1')
        self.assertEqual(issue_1.issue_content, 'Test 1')

        self.assertEqual(issue_2.team.team_name, 'Test')
        self.assertEqual(issue_2.issue_name, 'Test 2')
        self.assertEqual(issue_2.issue_content, 'Test 2')
