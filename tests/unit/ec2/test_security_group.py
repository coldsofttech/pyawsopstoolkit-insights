import unittest
from unittest.mock import patch

from pyawsopstoolkit_insights.ec2 import SecurityGroup


class TestSecurityGroup(unittest.TestCase):
    def setUp(self) -> None:
        from pyawsopstoolkit.account import Account
        from pyawsopstoolkit.session import Session

        self.profile_name = 'temp'
        self.account = Account('123456789012')
        self.session = Session(profile_name=self.profile_name)
        self.security_group = SecurityGroup(session=self.session)

    def test_initialization(self):
        self.assertEqual(self.security_group.session, self.session)

    def test_setters(self):
        from pyawsopstoolkit.session import Session

        new_session = Session(profile_name='sample')
        self.security_group.session = new_session
        self.assertEqual(self.security_group.session, new_session)

    def test_invalid_types(self):
        invalid_session = 123

        with self.assertRaises(TypeError):
            SecurityGroup(session=invalid_session)
        with self.assertRaises(TypeError):
            self.security_group.session = invalid_session

    @patch('boto3.Session')
    def test_unused_security_groups_no_security_groups_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(len(self.security_group.unused_security_groups()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.ec2.SecurityGroup')
    def test_unused_security_groups_no_groups_matching_criteria(self, mock_ec2, mock_session):
        from pyawsopstoolkit_models.ec2.security_group import SecurityGroup, IPPermission, IPRange

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        def mock_search_security_groups(include_usage=True, in_use=False):
            if include_usage:
                return []
            else:
                return [
                    SecurityGroup(
                        account=self.account,
                        region='eu-west-1',
                        id='sg-abcdef0123456789',
                        name='my-security-group',
                        owner_id='123456789012',
                        vpc_id='vpc-1a2b3c4d',
                        ip_permissions=[IPPermission(
                            from_port=22,
                            to_port=22,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='0.0.0.0/0'
                            )]
                        )],
                        ip_permissions_egress=[IPPermission(
                            from_port=0,
                            to_port=0,
                            ip_protocol='-1',
                            ip_ranges=[IPRange(
                                cidr_ip='0.0.0.0/0'
                            )]
                        )],
                        description='My first security group',
                        in_use=True
                    )
                ]

        mock_ec2.return_value.search_security_groups.return_value = mock_search_security_groups()

        self.assertEqual(len(self.security_group.unused_security_groups()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit_advsearch.ec2.SecurityGroup')
    def test_unused_security_groups_some_groups_matching_criteria(self, mock_ec2, mock_session):
        from pyawsopstoolkit_models.ec2.security_group import SecurityGroup, IPPermission, IPRange

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        def mock_search_security_groups(include_usage=True, in_use=False):
            if include_usage:
                return [
                    SecurityGroup(
                        account=self.account,
                        region='ap-southeast-2',
                        id='sg-fedcba9876543210',
                        name='db-access-sg',
                        owner_id='210987654321',
                        vpc_id='vpc-1b2c3d4e',
                        ip_permissions=[IPPermission(
                            from_port=3306,
                            to_port=3306,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='10.0.0.0/16'
                            )]
                        )],
                        ip_permissions_egress=[IPPermission(
                            from_port=1024,
                            to_port=65535,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='10.0.0.0/16'
                            )]
                        )],
                        description='Security group for database access',
                        in_use=False
                    )
                ]
            else:
                return [
                    SecurityGroup(
                        account=self.account,
                        region='us-east-1',
                        id='sg-1234567890abcdef',
                        name='web-server-sg',
                        owner_id='098765432109',
                        vpc_id='vpc-4d3c2b1a',
                        ip_permissions=[IPPermission(
                            from_port=80,
                            to_port=80,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='192.168.1.0/24'
                            )]
                        ), IPPermission(
                            from_port=443,
                            to_port=443,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='192.168.1.0/24'
                            )]
                        )],
                        ip_permissions_egress=[IPPermission(
                            from_port=0,
                            to_port=0,
                            ip_protocol='-1',
                            ip_ranges=[IPRange(
                                cidr_ip='0.0.0.0/0'
                            )]
                        )],
                        description='Security group for web server',
                        in_use=True
                    ),
                    SecurityGroup(
                        account=self.account,
                        region='eu-central-1',
                        id='sg-0987abcdef654321',
                        name='ssh-access-sg',
                        owner_id='567890123456',
                        vpc_id='vpc-5e4d3c2b',
                        ip_permissions=[IPPermission(
                            from_port=22,
                            to_port=22,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='203.0.113.0/24'
                            )]
                        )],
                        ip_permissions_egress=[IPPermission(
                            from_port=80,
                            to_port=80,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='0.0.0.0/0'
                            )]
                        ), IPPermission(
                            from_port=443,
                            to_port=443,
                            ip_protocol='tcp',
                            ip_ranges=[IPRange(
                                cidr_ip='0.0.0.0/0'
                            )]
                        )],
                        description='Security group for SSH and web traffic',
                        in_use=True
                    )
                ]

        mock_ec2.return_value.search_security_groups.return_value = mock_search_security_groups()

        self.assertEqual(len(self.security_group.unused_security_groups()), 1)


if __name__ == "__main__":
    unittest.main()
