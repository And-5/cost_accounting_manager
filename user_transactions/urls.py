from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('transaction/', TransactionListView.as_view()),
    path('transaction/create/', TransactionCreateView.as_view()),
    path('balance/', BalanceListView.as_view()),
]
