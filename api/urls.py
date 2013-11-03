from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
    url(r'^scores/$', views.ScoreList.as_view()),
    url(r'^scores/(?P<subject>[0-9]+)/(?P<value>[0-9]+)/$', views.ScorePost.as_view()),
    url(r'^quizzes/$', views.QuizList.as_view()),
    url(r'^quizzes/fractions/$', views.FractionQuiz.as_view()),
    url(r'^quizzes/multiplication/$', views.MultiplicationQuiz.as_view()),
    url(r'^quizzes/addition/$', views.AdditionQuiz.as_view()),
    url(r'^quizzes/subtraction/$', views.SubtractionQuiz.as_view()),
    url(r'^quizzes/division/$', views.DivisionQuiz.as_view()),
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
