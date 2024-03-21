from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InputData
from .serializers import InputDataSerializer

class GenerateAlternateDrug(APIView):
    def post(self, request):
        # Query the database for the first instance of InputData
        input_data = InputData.objects.first()

        if input_data:
            # If an instance is found, retrieve the alternate_drug field
            alternate_drug = input_data.alternate_drug

            # Create a dictionary response with the alternate_drug field
            response_data = {
                'alternate_drug': alternate_drug
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # If no instance is found, return an appropriate error response
            return Response({'error': 'No InputData found'}, status=status.HTTP_404_NOT_FOUND)