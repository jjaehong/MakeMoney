from django.shortcuts import render

import requests



from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.


# 데이터 보기
@api_view(['GET'])
def index(request):
    PRODUCT_API_KEY = 'c0aecf40a0bc63eecd50da8c11f5902d'

    deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(deposit_url).json()

    return Response(response.data)
