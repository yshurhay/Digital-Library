from django.contrib import admin
from .models.book import Book
from .models.genre import Genre
from .models.author import Author

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
