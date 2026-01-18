from django.contrib import admin
from .models import Book

# Custom admin for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # searchable fields
    list_filter = ('publication_year',)  # filter by year

