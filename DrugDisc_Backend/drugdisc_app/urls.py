from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import GenerateAlternateDrug
router=DefaultRouter()
urlpatterns = [
   path('',include(router.urls)),
 path('generate-alternate-drug/', GenerateAlternateDrug.as_view(), name='generate-alternate-drug'),
    # Add more paths for additional pages or functionality
]
