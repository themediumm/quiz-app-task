# quiz/urls.py

from django.urls import path
from .views import quiz_view, result_view

urlpatterns = [
    path('', quiz_view, name='quiz'),
    path('result/', result_view, name='result'),
]
