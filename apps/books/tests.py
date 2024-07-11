from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.books.models import Genre, Author, Book


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name='test genre'
        )

        self.author = Author.objects.create(
            first_name='Test name',
            last_name='Test surname'
        )

        self.book = Book.objects.create(
            title='Test title',
            author=self.author,
            genre=self.genre,
            year=1000,
            country='Test country',
            description='Test description',
            is_public=True
        )


class CreateBookTest(BaseTestSetup):
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'test',
            'author': self.author.pk,
            'genre': self.genre.pk,
            'year': 1000,
            'country': 'test',
            'description': 'test',
            'is_public': True
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateBookTest(BaseTestSetup):
    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})

        data = {
            'title': 'new test'
        }
        time_before = datetime.now()
        response = self.client.patch(url, data, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(time_before, time_after)


class DeleteBookTest(BaseTestSetup):
    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        time_before = datetime.now()
        response = self.client.delete(url, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(time_before, time_after)


class ReadBookTest(BaseTestSetup):
    def test_read_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
