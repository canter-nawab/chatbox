from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

app_name = 'chatbox'

urlpatterns = [
    path('', TemplateView.as_view(template_name='chatbox/login.html'), name='login'),
    path('conversations', views.new_user, name='loggedin'),
    path('newconvo', views.new_convo, name='new_convo'),
    #path('message', views.new_message, name='messages'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room')
]