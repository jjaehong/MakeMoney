from django.urls import path 
from . import views

# app_name = 'products'
urlpatterns = [
    path('',views.index),

    # 예적금 상품 목록 DB에 저장
    path('save-deposit-products/', views.save_deposit_products),
    path('save-savings-products/', views.save_savings_products),

    # 예적금 상품 목록 출력(GET) & 데이터 삽입(POST)
    path('product-list/', views.product_list),

    # 특정 상품의 옵션 리스트 출력
    path('product-options/<str:fin_prdt_cd>/', views.product_options),

    # 대출상품 DB 저장
    path('save-mortgage-loan/', views.save_mortgage_loan),
    path('save-jeonse-loan/', views.save_jeonse_loan),
    path('save-credit-loan/', views.save_credit_loan),

    # 대출 상품 목록 출력(GET) & 데이터 삽입(POST)
    path('loan-list/', views.loan_list),

    # 특정 대출 상품의 옵션 리스트 출력
    path('loan-options/<str:loan>/', views.loan_options),

    # 개인신용대출 상품 목록 출력(GET) & 데이터 삽입(POST)
    path('credit-loan-list/', views.credit_loan_list),

    # 특정 개인신용대출 상품의 옵션 리스트 출력
    path('credit-loan-options/<str:credit_loan>/', views.credit_loan_options),

]

