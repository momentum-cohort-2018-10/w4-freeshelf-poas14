from django.shortcuts import render
from bookings.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books,
    })

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

def choose_category(request):
    books = Book.objects.all()
    return render(request, 'choose_category.html', {
        'books': books,
    })

# def choose_category(request, book, slug):

#     category = book.objects.filter(category)
#     return render(request, 'categories/choose_category.html', {
#         'category': category,
#         'books': Book.objects.filter(categories__slug=category.slug)
#     })

# def choose_category(request, category):
#     catapult = Book.objects.filter(category=category)
#     return render(request, 'books/choose_category.html', {
#         'Python': catapult,
#     })
