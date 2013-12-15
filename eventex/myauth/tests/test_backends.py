# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='henrique',
                                      email='henrique@bastos.net',
                                      password='abracadabra')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='henrique@bastos.net',
                                         password='abracadabra')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(email='henrique@bastos.net',
                                         password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@email.com',
                                         password='abracadabra')
        self.assertIsNone(user)


class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
            email='henrique@bastos.net', password='abracadabra')
        UserModel.objects.create_user(username='user2',
            email='henrique@bastos.net', password='abracadabra')
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(email='henrique@bastos.net',
                                         password='abracadabra')
        self.assertIsNone(user)
