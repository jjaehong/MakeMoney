from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

import requests


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ProductListSerializer, ProductListOptionsSerializer, LoanListSerializer, LoanListOptionsSerializer, CreditLoanSerializer, CreditLoanOptionsSerializer
from .models import ProductList, ProductListOptions, Loan, LoanOptions, CreditLoan, CreditLoanOptions


# Create your views here.


# 데이터 확인
@api_view(['GET'])
def index(request):
    PRODUCT_API_KEY = settings.PRODUCT_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth=c0aecf40a0bc63eecd50da8c11f5902d&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    print(response)

    return Response(response)


# 예금 데이터 DB에 저장
def save_deposit_products(request):
    PRODUCT_API_KEY = settings.PRODUCT_API_KEY

    deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(deposit_url).json()

    for li in response.get("result").get('baseList'):
        print(li)
        data_baseList={
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'dcls_month' : li.get('dcls_month'),
            'kor_co_nm' : li.get('kor_co_nm'),           
            'fin_prdt_nm' : li.get('fin_prdt_nm'),         
            'etc_note' : li.get('etc_note'),     
            'join_deny'  : li.get('join_deny'),     
            'join_member' : li.get('join_member'),         
            'join_way' : li.get('join_way'),             
            'spcl_cnd' : li.get('spcl_cnd'),   
        }
        serializer_baseList = ProductListSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()

    for li in response.get("result").get('optionList'):
        print(li)
        products = ProductList.objects.get(fin_prdt_cd=li["fin_prdt_cd"])

        serializer_optionList = ProductListOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(product=products)
            
    return JsonResponse({ 'message': 'okay' })


# 적금 데이터 DB에 저장
def save_savings_products(request):
    PRODUCT_API_KEY = settings.PRODUCT_API_KEY

    savings_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(savings_url).json()

    for li in response.get("result").get('baseList'):
        data_baseList={
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'dcls_month' : li.get('dcls_month'),
            'kor_co_nm' : li.get('kor_co_nm'),           
            'fin_prdt_nm' : li.get('fin_prdt_nm'),         
            'etc_note' : li.get('etc_note'),     
            'join_deny'  : li.get('join_deny'),     
            'join_member' : li.get('join_member'),         
            'join_way' : li.get('join_way'),             
            'spcl_cnd' : li.get('spcl_cnd'),   
        }
        serializer_baseList = ProductListSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()

    for li in response.get("result").get('optionList'):
        # print(li["fin_prdt_cd"])
        products = ProductList.objects.get(fin_prdt_cd=li["fin_prdt_cd"])

        serializer_optionList = ProductListOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(product=products)
            
    return JsonResponse({ 'message': 'okay' })


# 주담대 데이터 DB에 저장
def save_mortgage_loan(request):
    PRODUCT_API_KEY = settings.PRODUCT_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    # print(response)
    for li in response.get("result").get("baseList"):
        data_baseList= {
        'fin_prdt_cd' : li.get('fin_prdt_cd'),
        'kor_co_nm' : li.get('kor_co_nm'),           
        'fin_prdt_nm' : li.get('fin_prdt_nm'),                
        'join_way' : li.get('join_way'),
        'loan_inci_expn' : li.get('loan_inci_expn'),
        'erly_rpay_fee' : li.get('erly_rpay_fee'),
        'dly_rate' : li.get('dly_rate'),
        'loan_lmt' : li.get('loan_lmt'),
        'dcls_month' : li.get('dcls_month'),
    }
        serializer_baseList = LoanListSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()

    for li in response.get("result").get('optionList'):
        # print(li)
        loan = Loan.objects.get(fin_prdt_cd=li["fin_prdt_cd"])

        serializer_optionList =LoanListOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(loan=loan)
            
    return JsonResponse({ 'message': 'okay' })


# 전세자금대출 DB에 저장
def save_jeonse_loan(request):
    PRODUCT_API_KEY = settings.PRODUCT_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    # print(response)
    for li in response.get("result").get("baseList"):
        data_baseList= {
        'fin_prdt_cd' : li.get('fin_prdt_cd'),
        'kor_co_nm' : li.get('kor_co_nm'),           
        'fin_prdt_nm' : li.get('fin_prdt_nm'),                
        'join_way' : li.get('join_way'),
        'loan_inci_expn' : li.get('loan_inci_expn'),
        'erly_rpay_fee' : li.get('erly_rpay_fee'),
        'dly_rate' : li.get('dly_rate'),
        'loan_lmt' : li.get('loan_lmt'),
        'dcls_month' : li.get('dcls_month'),
    }
        serializer_baseList = LoanListSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()

    for li in response.get("result").get('optionList'):
        print(li)
        loan = Loan.objects.get(fin_prdt_cd=li["fin_prdt_cd"])

        serializer_optionList =LoanListOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(loan=loan)
            
    return JsonResponse({ 'message': 'okay' })

# 개인신용대출 DB에 저장
def save_credit_loan(request):

    PRODUCT_API_KEY = settings.PRODUCT_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=050000&pageNo=1'
    response = requests.get(url).json()
    # print(response)
    for li in response.get("result").get("baseList"):
        data_baseList= {
        'fin_co_no' : li.get('fin_co_no'),           
        'fin_prdt_cd' : li.get('fin_prdt_cd'),
        'fin_prdt_nm' : li.get('fin_prdt_nm'),
        'kor_co_nm' : li.get('kor_co_nm'),                
        'join_way' : li.get('join_way'),
        'crdt_prdt_type' : li.get('crdt_prdt_type'),
        'crdt_prdt_type_nm' : li.get('crdt_prdt_type_nm'),
        'dcls_month' : li.get('dcls_month'),
    }
        serializer_baseList = CreditLoanSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()

    for li in response.get("result").get('optionList'):
        print(li)
        credit_loan = CreditLoan.objects.get(fin_co_no=li["fin_co_no"])

        serializer_optionList =CreditLoanOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(credit_loan=credit_loan)
            
    return JsonResponse({ 'message': 'okay' })


# 전체 정기예적금 상품 목록 출력 & 데이터 삽입
@api_view(['GET','POST'])
def product_list(request):
    
    if request.method == 'GET':
        products = ProductList.objects.all()
        serializer = ProductListSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 특정 예적금 상품의 옵션 리스트 출력
@api_view(['GET'])
def product_options(request,fin_prdt_cd):
    if request.method == 'GET':
        options = ProductListOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = ProductListOptionsSerializer(options, many = True)
        return Response(serializer.data)
    

# 전체 대출상품 목록 출력 & 데이터 삽입
@api_view(['GET','POST'])
def loan_list(request):
    
    if request.method == 'GET':
        products = Loan.objects.all()
        serializer = LoanListSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LoanListSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 특정 대출상품의 옵션 리스트 출력
@api_view(['GET'])
def loan_options(request,loan):
    
    if request.method == 'GET':

        options = LoanOptions.objects.filter(loan=loan)
        serializer = LoanListOptionsSerializer(options, many = True)
        return Response(serializer.data)
    

# 전체 개인신용대출 상품 목록 출력 & 데이터 삽입
@api_view(['GET','POST'])
def credit_loan_list(request):
    
    if request.method == 'GET':
        products = CreditLoan.objects.all()
        serializer = CreditLoanSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CreditLoanSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 특정 대출상품의 옵션 리스트 출력
@api_view(['GET'])
def credit_loan_options(request,credit_loan):
    
    if request.method == 'GET':

        options = CreditLoanOptions.objects.filter(credit_loan=credit_loan)
        serializer = CreditLoanOptionsSerializer(options, many = True)
        return Response(serializer.data)