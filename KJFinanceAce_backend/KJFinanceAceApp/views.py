from rest_framework.response import Response
from rest_framework import views, status
from .models import InvestmentInfo
from .serializers import InvestmentInfoSerializer

class InvestmentInfoAPI(views.APIView):
    def get(self, request):
        investment_info = InvestmentInfo.objects.all()
        serializer = InvestmentInfoSerializer(investment_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvestmentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
