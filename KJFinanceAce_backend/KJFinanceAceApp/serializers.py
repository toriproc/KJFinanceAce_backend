from rest_framework import serializers
from .models import InvestmentInfo

class InvestmentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentInfo
        fields = ['key', 'date', 'name', 'totalInvestmentAmount', 'genzaiAmount']
