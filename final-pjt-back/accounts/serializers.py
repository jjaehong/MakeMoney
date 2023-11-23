from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('username', 'nickname' ,'email', 'age','money', 'salary','financial_products', 'loan_money', 'consumption','id', 'goal_money', 'goal_period')
