from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.quiz_test, name='quiz_test'),
    path('<int:id>/<int:qid>/', views.quiz_question, name='quiz_question'),
]
