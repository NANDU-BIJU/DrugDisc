from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InputData
from .serializers import InputDataSerializer

class GenerateAlternateDrug(APIView):
    def post(self, request):
        input_data = InputData.objects.first()

        if input_data:
            alternate_drug = input_data.alternate_drug
            response_data = {
                'alternate_drug': alternate_drug
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No InputData found'}, status=status.HTTP_404_NOT_FOUND)