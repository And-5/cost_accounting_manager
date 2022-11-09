from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters


from user_transactions.serializers import *
from rest_framework import generics, status

from .services import make_transaction


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionListView(generics.ListAPIView):
    queryset = UserTransactions.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['time', 'sum', 'date']
    ordering_fields = ['time', 'sum', 'date']


class TransactionCreateView(generics.CreateAPIView):
    queryset = UserTransactions.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        owner = self.request.user
        sum = float(self.request.data['sum'])
        category = self.request.data['category']
        organization = self.request.data['organization']
        description = self.request.data['description']
        time = self.request.data['time']
        date = self.request.data['date']
        error = {'error': 'Not enough money'}
        if make_transaction(
                owner,
                sum,
                time,
                date,
                category,
                organization,
                description,
        ):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class BalanceListView(generics.ListAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset
