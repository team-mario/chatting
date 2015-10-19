__author__ = 'judelee'

from django.test import TestCase
from team.models import UserInfo


class UserModelTest(TestCase):

    def test_can_save_and_retrieve_user_info(self):
        user_info_1 = UserInfo.objects.create(user_id='12121212121', user_name='judelee')
        self.assertEqual(
            list(UserInfo.objects.all()),
            [user_info_1]
        )
        same_user = UserInfo.objects.get(user_id='12121212121')
        self.assertEqual(user_info_1, same_user)
