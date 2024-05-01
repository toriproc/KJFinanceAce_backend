from rest_framework.response import Response
from rest_framework import views
from .models import InvestmentInfo
from .serializers import InvestmentInfoSerializer

class InvestmentInfoAPI(views.APIView):
    def get(self, request):
        investment_info = InvestmentInfo.objects.all()
        serializer = InvestmentInfoSerializer(investment_info, many=True)
        return Response(serializer.data)
