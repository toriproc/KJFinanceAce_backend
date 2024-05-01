from rest_framework import serializers
from .models import InvestmentInfo

class InvestmentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentInfo
        fields = ['date', 'name', 'total_investment_amount', 'genzai_amount']
