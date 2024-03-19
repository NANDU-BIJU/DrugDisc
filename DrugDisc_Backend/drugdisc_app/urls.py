from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (InputDataViewset)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('input-data-view',InputDataViewset,basename='input-data-view')
urlpatterns = [
   path('',include(router.urls)),

    # Add more paths for additional pages or functionality
]
