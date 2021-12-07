from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('drwing_app/drawing/', views.drawing, name="drawing"),
    path('catch-the-insect/game/', views.catch, name="catch"),
    path('quiz-let/quiz_app/quiz/app/game/', views.quiz, name="quiz"),
]