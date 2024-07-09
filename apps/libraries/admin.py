from django.contrib import admin
from .models import Library, BookInstance, UserLibrary

admin.site.register(Library)
admin.site.register(BookInstance)
admin.site.register(UserLibrary)
