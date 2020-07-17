from django.urls import path
from .views import TestView, DemoQuiz

urlpatterns = [
    path('', TestView.as_view(), name="quiz"),
    path('demo_test', DemoQuiz.as_view(), name='demo_test'),
]
