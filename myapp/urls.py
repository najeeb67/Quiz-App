from django.urls import path
from .views import home, take_quiz, api_question

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:id>/', take_quiz, name='take_quiz'),
    path('api/course/<int:id>/', api_question, name='api_question')
]
