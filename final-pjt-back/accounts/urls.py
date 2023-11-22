from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:user_pk>/', views.update)
]
