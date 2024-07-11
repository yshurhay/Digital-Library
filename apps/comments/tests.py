from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.books.models import Genre, Author, Book
from apps.users.models import User
from apps.comments.models import Comment


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name='test genre'
        )

        self.user = User.objects.create(
            email='test@test.com',
            first_name='test1',
            last_name='test2'
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

        self.comment = Comment.objects.create(
            user=self.user,
            book=self.book,
            text='test text'
        )


class CreateCommentTest(BaseTestSetup):
    def test_create_comment(self):
        url = reverse('comment-list')
        data = {
            'user': self.user.pk,
            'book': self.book.pk,
            'text': 'test'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateCommentTest(BaseTestSetup):
    def test_update_comment(self):
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})

        data = {
            'text': 'new test text'
        }
        time_before = datetime.now()
        response = self.client.patch(url, data, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(time_before, time_after)


class DeleteCommentTest(BaseTestSetup):
    def test_delete_comment(self):
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        time_before = datetime.now()
        response = self.client.delete(url, format='json')
        time_after = datetime.now()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(time_before, time_after)


class ReadCommentTest(BaseTestSetup):
    def test_read_comment_list(self):
        url = reverse('comment-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_comment_detail(self):
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
