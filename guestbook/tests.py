import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from guestbook.models import GuestBook
from guestbook.serializers import GuestBookRetrieveUpdateDestroySerializer, GuestBookListCreateSerializer

client = Client()


class GetAllGuestBookTest(TestCase):

    def setUp(self):
        GuestBook.objects.create(
            name='Test Name 1', subject='Test Subject 1', message='Test Message 1')
        GuestBook.objects.create(
            name='Test Name 2', subject='Test Subject 1', message='Test Message 2')
        GuestBook.objects.create(
            name='Test Name 3', subject='Test Subject 3', message='Test Message 3')
        GuestBook.objects.create(
            name='Test Name 4', subject='Test Subject 4', message='Test Message 4')

    def test_get_all_guestbooks(self):
        response = client.get(reverse('guestbook_list_create_api_view'))
        obj = GuestBook.objects.all()
        serializer = GuestBookListCreateSerializer(obj, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewGuestBookTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Name Surname',
            'subject': 'Test Subject',
            'message': 'Test Case Message'
        }
        self.invalid_payload = {
            'name': '',
            'subject': 'Test Subject',
            'message': 'Test Case Message'
        }

    def test_create_valid_guestbook(self):
        response = client.post(
            reverse('guestbook_list_create_api_view'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_guestbook(self):
        response = client.post(
            reverse('guestbook_list_create_api_view'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleGuestBookTest(TestCase):

    def setUp(self):
        self.obj = GuestBook.objects.create(
            name='Name Surname', subject="Test Subject", message='Test Case Message')

    def test_get_valid_single_guestbook(self):
        response = client.get(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': self.obj.id}))
        obj = GuestBook.objects.get(pk=self.obj.pk)
        serializer = GuestBookRetrieveUpdateDestroySerializer(obj)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_guestbook(self):
        response = client.get(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': 'b1bb9ea7-0a40-443b-bd26-acaac2e8c9bc'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleGuestBookTest(TestCase):

    def setUp(self):
        self.obj1 = GuestBook.objects.create(
            name='Test Name 1', subject='Test Subject 1', message='Test Message 1')
        self.obj2 = GuestBook.objects.create(
            name='Test Name 2', subject='Test Subject 1', message='Test Message 2')
        self.valid_payload = {
            'name': 'Test Name 1',
            'subject': 'Test Subject 1',
            'message': 'Test Message 2'
        }
        self.invalid_payload = {
            'name': '',
            'subject': 'Test Subject 1',
            'message': 'Test Message 2'
        }

    def test_valid_update_guestbook(self):
        response = client.put(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': str(self.obj1.id)}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_guestbook(self):
        response = client.put(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': str(self.obj1.id)}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleGuestBookTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.obj = GuestBook.objects.create(
            name='Test Name', subject='Test Subject', message='Test Message')

    def test_valid_delete_guestbook(self):
        response = client.delete(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': self.obj.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_(self):
        response = client.delete(
            reverse('guestbook_retrieve_update_destroy_api_view', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
