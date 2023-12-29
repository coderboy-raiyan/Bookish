from django.urls import path
from .views import DepositView, BorrowView

urlpatterns = [
    path("deposit/", DepositView.as_view(), name="deposit"),
    path("borrow/<int:id>", BorrowView.as_view(), name="borrow"),
]
