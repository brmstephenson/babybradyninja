from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
