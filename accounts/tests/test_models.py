from django.test import TestCase
from accounts.models import User


class AccountModelTest(TestCase):
    # Create user successfully
    def test_account_create_user(self):
        user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertIsNotNone(user.id)

    # # User password hashing works
    # def test_password_is_hashed(self):
    #     user = User.objects.create_user(
    #         username='testuser',
    #         password='pass123'
    #     )
    #     self.assertNotEqual(user.password,'pass123')
    #     self.assertEqual(user.check_password('pass123'))

    def test_account_create_superuser(self):
        admin_user = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="adminpass",
            is_staff=True,
            is_superuser=True,
        )
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

    def test_create_without_username(self):
        # if email is required in your model
        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                username=None, password="testuserpass", email="testuser@gmail.com"
            )

    def test_create_without_email(self):
        # if email is required in your model
        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                username="testuser", password="testuserpass", email=None
            )