from django.contrib import admin
# Register your models here.
from bookings.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'author', 'description', 'category', 'url', 'date')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, BookAdmin)