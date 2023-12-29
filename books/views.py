from django.shortcuts import render
from django.views.generic import DetailView
from .models import BookModel
# Create your views here.


class BookDetailsView(DetailView):
    template_name = "books/book_details.html"
    model = BookModel
    pk_url_kwarg = "id"
    context_object_name = "book"
