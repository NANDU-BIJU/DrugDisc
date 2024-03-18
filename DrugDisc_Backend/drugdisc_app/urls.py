from django.urls import path
from .views import input_data, result

urlpatterns = [
    path('', input_data, name='input_data'),
    path('result/', result, name='result'),
    # Add more paths for additional pages or functionality
]
