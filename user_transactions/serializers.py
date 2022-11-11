from rest_framework import serializers

from user_transactions.models import *


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = UserTransactions
        fields = ['sum', 'time', 'date', 'category', 'organization', 'description']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['balance']
