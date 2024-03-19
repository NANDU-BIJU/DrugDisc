from rest_framework import generics,mixins,viewsets,status
from .models import (InputData)
from .serializers import (InputDataSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView


class InputDataViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=InputDataSerializer
    queryset=InputData.objects.all()