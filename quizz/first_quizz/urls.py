from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('<int:id>/', views.quiz_test, name='quiz_test'),
                  path('tag/<slug:tag_slug>/',
                       views.quiz_test, name='quiz_test_by_tag'),
                  path('<int:id>/<int:qid>/', views.quiz_question, name='quiz_question'),
                  path('tag/<slug:tag_slug>/',
                       views.quiz_question, name='quiz_question_by_tag'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
