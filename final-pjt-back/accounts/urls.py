from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:user_pk>/', views.update),
    path('<int:user_pk>/', views.user)
]
