from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 유저 커스터마이징
class User(AbstractUser):
    
    # 고객 개인정보
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=50, unique=True, null=True)
    email = models.CharField(max_length=250, blank=True, null= True)
    age = models.IntegerField(blank=True,null=True)
    money = models.IntegerField(blank=True,null=True) # 자산
    salary = models.IntegerField(blank=True, null=True) # 연봉(연소득)
    consumption = models.IntegerField(blank=True, null=True) # 연소비 
    # 소비성향 : 소비/소득 => 단기금리가 상대적으로 높은 상품 추천
    # 저축성향 : 1 - 소비/소득(소비성향) => 장기금리가 상대적으로 높은 상품 추천
    
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True) # 예적금 상품목록
    loan_products =  models.TextField(blank=True, null=True) # 

    loan_money = models.IntegerField(blank=True, null=True) # 대출금
    goal_money = models.IntegerField(blank=True, null=True) # 목표금액
    goal_period = models.IntegerField(blank=True, null=True) # 목표기간
    

    # superuser fields
    # 활성화된 사용자
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
