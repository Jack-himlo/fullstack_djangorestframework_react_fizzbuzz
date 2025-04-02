from django.urls import path
from .views import FizzBuzzView


urlpatters = [
    path('fizzbuzz/', FizzBuzzView.as_view(), name='fizzbuzz')
]