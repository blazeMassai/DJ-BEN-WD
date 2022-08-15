from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .utils import average_rating


# Create your views here.
def index(request):
    return render(request, 'base.html')


def book_list(request):
    books = Book.objects.all()
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews
