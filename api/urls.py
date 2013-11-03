from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
    url(r'^quizzes/?', views.QuizList.as_view()),
    url(r'^quizzes/fractions/$', views.FractionQuiz.as_view()),
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
