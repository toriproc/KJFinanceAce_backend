from django.urls import path
from .views import InvestmentInfoAPI

urlpatterns = [
    path('get-investment-info/', InvestmentInfoAPI.as_view(), name='get-investment-info'),
    path('get-investment-info/<int:pk>/', InvestmentInfoAPI.as_view(), name='get-investment-info')
    # 他のエンドポイントを追加することもできます
]
