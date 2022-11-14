from rest_framework import serializers

from user_transactions.models import *


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserTransactions
        fields = ['owner', 'sum', 'time', 'date', 'category', 'organization', 'description']

    def __init__(self, *args, **kwargs):
        super(TransactionSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        if not user.is_staff:
            self.fields['category'].queryset = Category.objects.filter(owner=user)


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['balance']
