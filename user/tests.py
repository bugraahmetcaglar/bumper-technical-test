import datetime
import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from user.models import User
from user.serializers import UserRegisterSerializer, UserListSerializer, UserDetailSerializer

client = Client()


class GetAllUsersTest(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='First Name 1', last_name='Last Name 1', email='test1@email.com', username='test_username1'
        )
        User.objects.create(
            first_name='First Name 2', last_name='Last Name 2', email='test2@email.com', username='test_username2'
        )
        User.objects.create(
            first_name='First Name 3', last_name='Last Name 3', email='test3@email.com', username='test_username3'
        )
        User.objects.create(
            first_name='First Name 4', last_name='Last Name 4', email='test4@email.com', username='test_username4'
        )

    def test_get_all_users(self):
        response = client.get(reverse('user_list_api'))
        obj = User.objects.all()
        serializer = UserListSerializer(obj, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewUserTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'test@email.com',
            'username': 'test_username',
            'password': 'test.pass123',
            'password2': 'test.pass123',
        }
        self.invalid_payload = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'test2@email.com',
            'username': '',
            'password': 'test.pass321',
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('user_create_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('user_create_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleUserTest(TestCase):

    def setUp(self):
        self.obj = User.objects.create(
            first_name='First', last_name='Last', email='test4@email.com', username='username',
            date_joined=datetime.datetime.now(),
            last_login=datetime.datetime.now()
        )

    def test_get_valid_single_user(self):
        response = client.get(
            reverse('user_detail_api', kwargs={'id': self.obj.id}))
        obj = User.objects.get(pk=self.obj.pk)
        serializer = UserListSerializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('user_detail_api', kwargs={'id': '50'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

