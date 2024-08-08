from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.quiz_test, name='quiz_test'),
    path('<int:id>/<int:qid>/', views.quiz_question, name='quiz_question'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
