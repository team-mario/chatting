__author__ = 'judelee'
from django.test import TestCase
from team.models import IssueChannel, HashTag
from django.contrib.auth.models import User


class HashTagTest(TestCase):

    def test_hash_tags_can_saved_into_multiple_channels(self):
        # Many to many relationships.
        hash_1 = HashTag(tag_name='soma06')
        hash_2 = HashTag(tag_name='team-mario')
        hash_3 = HashTag(tag_name='mac')

        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.get(username='john')

        channel_1 = IssueChannel.objects.create(user=user, channel_name='channel_1')
        channel_2 = IssueChannel.objects.create(user=user, channel_name='channel_2')
        channel_3 = IssueChannel.objects.create(user=user, channel_name='channel_3')
        hash_1.save()
        hash_2.save()
        hash_3.save()
        hash_1.channels.add(channel_1)
        hash_1.channels.add(channel_2, channel_3)
        hash_2.channels.add(channel_2)
        hash_3.channels.add(channel_3)

        self.assertEqual(
            list(hash_1.channels.all()),
            [channel_1, channel_2, channel_3]
        )
        self.assertEqual(
            list(hash_2.channels.all()),
            [channel_2]
        )
        self.assertNotEqual(
            list(hash_2.channels.all()),
            [channel_3]
        )
        self.assertEqual(
            list(hash_3.channels.all()),
            [channel_3]
        )
