from rest_framework import serializers
from .models import ProductList, ProductListOptions, Loan, LoanOptions, CreditLoan, CreditLoanOptions


class ProductListSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductList
        fields = '__all__'
        read_only_fields = ('product_type',)


class ProductListOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductListOptions
        fields = '__all__'
        read_only_fields = ('product',)


class LoanListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Loan
        fields = '__all__'


class LoanListOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = LoanOptions
        fields = '__all__'
        read_only_fields = ('loan',)


class CreditLoanSerializer(serializers.ModelSerializer):
    class Meta():
        model = CreditLoan
        fields = '__all__'


class CreditLoanOptionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = CreditLoanOptions
        fields = '__all__'
        read_only_fields = ('credit_loan',)