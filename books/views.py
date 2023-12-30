from django.shortcuts import render
from django.views.generic import DetailView
from .models import BookModel
from django.contrib.auth.decorators import login_required
from transactions.models import TransactionModel
# Create your views here.


class BookDetailsView(DetailView):
    template_name = "books/book_details.html"
    model = BookModel
    pk_url_kwarg = "id"
    context_object_name = "book"


# def returnBook(request, id) :
#     transaction = TransactionModel.objects.get(pk=id)
