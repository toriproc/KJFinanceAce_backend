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

    def delete(self, request, pk):
        try:
            investment_info_obj = InvestmentInfo.objects.get(pk=pk)
        except InvestmentInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        investment_info_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            investment_info_obj = InvestmentInfo.objects.get(pk=pk)
        except InvestmentInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        investment_info_obj.key = request.data.get('key', investment_info_obj.key)
        investment_info_obj.date = request.data.get('date', investment_info_obj.date)
        investment_info_obj.name = request.data.get('name', investment_info_obj.name)
        investment_info_obj.totalInvestmentAmount = request.data.get('totalInvestmentAmount', investment_info_obj.totalInvestmentAmount)
        investment_info_obj.genzaiAmount = request.data.get('genzaiAmount', investment_info_obj.genzaiAmount)
        # 保存
        investment_info_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
