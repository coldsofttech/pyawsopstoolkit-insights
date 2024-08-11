import unittest
from datetime import datetime
from unittest.mock import patch

from pyawsopstoolkit_insights.iam import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        from pyawsopstoolkit.account import Account
        from pyawsopstoolkit.session import Session

        self.profile_name = 'temp'
        self.account = Account('123456789012')
        self.session = Session(profile_name=self.profile_name)
        self.user = User(session=self.session)

    def test_initialization(self):
        self.assertEqual(self.user.session, self.session)

    def test_setters(self):
        from pyawsopstoolkit.session import Session

        new_session = Session(profile_name='sample')
        self.user.session = new_session
        self.assertEqual(self.user.session, new_session)

    def test_invalid_types(self):
        invalid_session = 123

        with self.assertRaises(TypeError):
            User(session=invalid_session)
        with self.assertRaises(TypeError):
            self.user.session = invalid_session

    @patch('boto3.Session')
    def test_unused_users_no_iam_users_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(len(self.user.unused_users()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_no_users_matching_criteria1(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            )
        ]

        self.assertEqual(len(self.user.unused_users()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_no_users_matching_criteria2(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User, LoginProfile

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                login_profile=LoginProfile(
                    created_date=datetime.today()
                )
            )
        ]

        self.assertEqual(len(self.user.unused_users()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_no_users_matching_criteria3(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            )
        ]

        self.assertEqual(len(self.user.unused_users()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_no_users_matching_criteria4(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User, AccessKey

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            )
        ]

        self.assertEqual(len(self.user.unused_users()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_some_roles_matching_criteria(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User, LoginProfile, AccessKey

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user1',
                id='ABDCGHY',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user1',
                created_date=datetime(2022, 5, 18),
                login_profile=LoginProfile(
                    created_date=datetime.today()
                )
            ),
            User(
                account=self.account,
                name='test_user2',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user2',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            ),
            User(
                account=self.account,
                name='test_user3',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user3',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            ),
            User(
                account=self.account,
                name='test_user4',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user4',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime(2022, 5, 20)
            ),
            User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime(2022, 5, 18)
            ),
            User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime.today()
            )
        ]

        self.assertEqual(len(self.user.unused_users()), 2)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.iam.User')
    def test_unused_users_some_roles_matching_criteria_include_newly_created(self, mock_iam, mock_session):
        from pyawsopstoolkit_models.iam.user import User, LoginProfile, AccessKey

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_users.return_value = [
            User(
                account=self.account,
                name='test_user1',
                id='ABDCGHY',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user1',
                created_date=datetime(2022, 5, 18),
                login_profile=LoginProfile(
                    created_date=datetime.today()
                )
            ),
            User(
                account=self.account,
                name='test_user2',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user2',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            ),
            User(
                account=self.account,
                name='test_user3',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user3',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            ),
            User(
                account=self.account,
                name='test_user4',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user4',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime(2022, 5, 20)
            ),
            User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime(2022, 5, 18)
            ),
            User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime.today()
            )
        ]

        self.assertEqual(len(self.user.unused_users(include_newly_created=True)), 3)


if __name__ == "__main__":
    unittest.main()
