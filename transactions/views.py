from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import TransactionModel
from .forms import DepositForm, BorrowForm
from .constants import DEPOSIT, RETURN, BORROW
from django.contrib import messages
from django.urls import reverse_lazy
from books.models import BookModel
# Create your views here.


class TransactionViewMixin(LoginRequiredMixin, CreateView):
    template_name = "transactions/transaction_form.html"
    success_url = reverse_lazy("home")
    model = TransactionModel
    title = ""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'customer': self.request.user.customer
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context


class DepositView(TransactionViewMixin):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        customer = self.request.user.customer

        customer.balance += amount

        customer.save(
            update_fields=['balance']
        )

        messages.success(self.request, f"""{"{:,.2f}".format(
            float(amount))}$ was deposited to your account successfully""")

        return super().form_valid(form)


class BorrowView(TransactionViewMixin):
    form_class = BorrowForm
    title = "Borrow Book"

    def get_initial(self):
        id = self.kwargs['id']
        book = BookModel.objects.get(id=id)
        initial = {'transaction_type': BORROW,
                   'book': book, 'amount': book.borrowing_price}
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        book = BookModel.objects.get(id=id)
        context.update({
            'book': book,
            'isBookView': True
        })
        return context

    def form_valid(self, form):
        customer = self.request.user.customer
        id = self.kwargs['id']
        book = BookModel.objects.get(id=id)
        # Get the amount from the form
        amount = book.borrowing_price

        customer.balance -= amount

        customer.save(
            update_fields=['balance']
        )

        messages.success(self.request, f""" Book has been borrowed and your current amount is ${
                         customer.balance} """)

        return super().form_valid(form)
