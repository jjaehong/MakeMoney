from django.db import models

# Create your models here.

# 예적금 상품정보
class ProductList(models.Model):
    fin_prdt_cd = models.TextField(primary_key=True)                            # 금융 상품 코드
    product_type = models.IntegerField(default=-1, blank=True, null=True)       # 상품 유형(예금,적금)
    kor_co_nm = models.TextField(default=-1, blank=True, null=True)             # 금융 회사명
    fin_prdt_nm = models.TextField(default=-1, blank=True, null=True)           # 금융 상품명
    etc_note = models.TextField(default=-1, blank=True, null=True)              # 금융 상품 설명
    join_deny  = models.IntegerField(default=-1, blank=True, null=True)         # 가입제한(1:제한없음, 2: 서민전용, 3:일부제한)
    join_member = models.TextField(default=-1, blank=True, null=True)           # 가입 대상
    join_way = models.TextField(default=-1, blank=True, null=True)              # 가입 방법
    spcl_cnd = models.TextField(default=-1, blank=True, null=True)              # 우대 조건
    dcls_month = models.TextField(default=-1, blank=True, null=True)            # 공시 제출월


# 예적금 옵션목록
class ProductListOptions(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)          # 외래 키(ProductList 클래스참조)
    fin_prdt_cd = models.TextField(default=-1, blank=True, null=True)           # 금융 상품 코드
    intr_rate_type_nm = models.CharField(default=-1, blank=True, null=True,max_length=100) # 저축 금리 유형명(단리,복리)
    intr_rate = models.FloatField(default=-1, blank=True, null=True)            # 저축 금리
    intr_rate2 = models.FloatField(default=-1, blank=True, null=True)           # 최고우대금리
    save_trm = models.IntegerField(default=-1, blank=True, null=True)           # 저축기간 (단위 : 개월)
