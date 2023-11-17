from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    # 유저 커스터마이징
    # id는 그냥 있음
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=50, unique=True, null=True)
    email = models.CharField(max_length=250, blank=True, null= True)
    age = models.IntegerField(blank=True,null=True)
    money = models.IntegerField(blank=True,null=True)
    salary = models.IntegerField(blank=True, null=True)
    
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    # 활성화된 사용자
    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
