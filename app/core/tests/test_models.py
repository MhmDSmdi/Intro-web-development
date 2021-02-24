from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'test12345678'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            email = None
            password = 'test12345678'
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )
    
    def test_create_new_superuser(self):
        email = 'admin@gmail.com'
        password = 'test12345678'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)