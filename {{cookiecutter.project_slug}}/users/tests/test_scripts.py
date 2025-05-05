from django.test import TestCase
from users.scripts import create_admin


class TestScripts(TestCase):

    def setUp(self):
        self.admin_dict = {
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com'
        }

    def test_create_admin(self):
        """
        Test create_admin: success: admin created
        :return:
        """
        admin, created = create_admin(**self.admin_dict)
        self.assertTrue(created)
        self.assertEqual('admin', admin.username)
        self.assertEqual('admin@admin.com', admin.email)
        self.assertTrue(admin.is_superuser)

    def test_create_admin_exists(self):
        """
        Test create_admin: success: already created
        :return:
        """
        admin, created = create_admin(**self.admin_dict)
        self.assertTrue(created)

        admin, created = create_admin(**self.admin_dict)
        self.assertFalse(created)
        self.assertTrue(admin.is_superuser)
        self.assertEqual('admin', admin.username)
