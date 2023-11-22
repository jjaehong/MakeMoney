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
    save_trm = models.IntegerField(default=-1, blank=True, null=True)         # 저축기간 (단위 : 개월)


# 주담대 & 전세자금 대출 상품정보
class Loan(models.Model):
    fin_prdt_cd = models.TextField(primary_key=True)                            # 금융상품 코드 pk
    kor_co_nm = models.TextField(default=-1, blank=True, null=True)             # 금융 회사명
    fin_prdt_nm = models.TextField(default=-1, blank=True, null=True)           # 금융상품 명
    join_way = models.TextField(default=-1, blank=True, null=True)              # 가입 방법
    loan_inci_expn = models.TextField(default=-1, blank=True, null=True)        # 대출 부대비용
    erly_rpay_fee = models.TextField(default=-1, blank=True, null=True)         # 중도상환 수수료
    dly_rate = models.TextField(default=-1, blank=True, null=True) # 연체 이자율
    loan_lmt = models.TextField(default=-1, blank=True, null=True) # 대출한도
    dcls_month = models.TextField(default=-1, blank=True, null=True) # 공시제출월 


# 주담대 & 전세자금 대출 옵션 목록
class LoanOptions(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE) # 포린키
    mrtg_type = models.TextField(default=-1, blank=True, null=True) # 담보유형 코드(apart, etc, ) => default -1
    mrtg_type_nm = models.TextField(default=-1, blank=True, null=True) # 담보 유형(아파트/ 아파트 외) => default -1
    rpay_type = models.TextField(default=-1, blank=True, null=True) # 대출 상환유형 코드
    rpay_type_nm = models.TextField(default=-1, blank=True, null=True) # 대출 상환 유형(분할상환방식)
    lend_rate_type = models.TextField(default=-1, blank=True, null=True) # 대출 금리 유형 코드
    lend_rate_type_nm = models.TextField(default=-1, blank=True, null=True) # 대출금리유형(고정금리, 변동금리)
    lend_rate_min = models.FloatField(default=-1, blank=True, null=True) # 대출금리 최저
    lend_rate_max = models.FloatField(default=-1, blank=True, null=True) # 대출금리 최고
    lend_rate_avg = models.FloatField(default=-1, blank=True, null=True) # 전월 취급 평균금리


# 개인신용대출 상품 목록
class CreditLoan(models.Model):
    kor_co_nm = models.TextField(default=-1, blank=True, null=True)  # 금융회사 명
    fin_co_no = models.TextField(default=-1, blank=True, null=True)  # 금융회사 코드
    fin_prdt_cd = models.TextField(default=-1, blank=True, null=True)  # 금융상품 코드 
    fin_prdt_nm = models.TextField(default=-1, blank=True, null=True) # 금융상품 명
    join_way = models.TextField(default=-1, blank=True, null=True) # 가입 방법
    crdt_prdt_type = models.TextField(default=-1, blank=True, null=True) # 대출종류 코드
    crdt_prdt_type_nm = models.TextField(default=-1, blank=True, null=True) # 대출중류 명
    dcls_month = models.TextField(default=-1, blank=True, null=True) # 공시제출월


# 개인신용대출 옵션 목록
class CreditLoanOptions(models.Model):
    credit_loan = models.ForeignKey(CreditLoan, on_delete=models.CASCADE) # 포린키
    fin_co_no = models.TextField(default=-1, blank=True, null=True) # 금융회사명으로 구분해야함
    crdt_lend_rate_type = models.TextField(default=-1, blank=True, null=True) # 금리구분 코드
    crdt_lend_rate_type_nm = models.TextField(default=-1, blank=True, null=True) # 금리 구분
    crdt_grad_1 = models.FloatField(default=-1, blank=True, null=True)# 900점 초과(float)
    crdt_grad_4 = models.FloatField(default=-1, blank=True, null=True)# 8-900
    crdt_grad_5 = models.FloatField(default=-1, blank=True, null=True)# 7-800
    crdt_grad_6 = models.FloatField(default=-1, blank=True, null=True)# 6-700
    crdt_grad_10 = models.FloatField(default=-1, blank=True, null=True)# 5-600
    crdt_grad_11 = models.FloatField(default=-1, blank=True, null=True)# 4-500
    crdt_grad_12 = models.FloatField(default=-1, blank=True, null=True)# 3-400
    crdt_grad_13 = models.FloatField(default=-1, blank=True, null=True) # 300 이하
    crdt_grad_avg = models.FloatField(default=-1, blank=True, null=True) #평균금리