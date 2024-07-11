from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.libraries.models import Library


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.library = Library.objects.create(
            name='test name',
            address='test address'
        )


class CreateLibraryTest(BaseTestSetup):
    def test_create_library(self):
        url = reverse('library-list')
        data = {
            'name': 'test',
            'address': 'test'
        }

        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateLibraryTest(BaseTestSetup):
    def test_update_library(self):
        url = reverse('library-detail', kwargs={'pk': self.library.pk})
        data = {
            'name': 'new name'
        }
        time_before = datetime.now()
        response = self.client.patch(url, data, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(time_before, time_after)


class DeleteLibraryTest(BaseTestSetup):
    def test_delete_library(self):
        url = reverse('library-detail', kwargs={'pk': self.library.pk})
        time_before = datetime.now()
        response = self.client.delete(url, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(time_before, time_after)


class ReadLibraryTest(BaseTestSetup):
    def test_read_library_list(self):
        url = reverse('library-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_library_detail(self):
        url = reverse('library-detail', kwargs={'pk': self.library.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
