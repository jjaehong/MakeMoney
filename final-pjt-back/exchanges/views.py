from django.shortcuts import render
from django.conf import settings

from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


import requests
# Create your views here.

@api_view(['GET'])
def exchange_currency(request):

    EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
    
    exchange_url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?data=AP01&authkey={EXCHANGE_API_KEY}'
    response_data = requests.get(exchange_url).json()

    

    return Response(response_data)

