from django.conf.urls import url
from django.urls import path
from . import consumers

app_name = 'chatbox'

websocket_urlpatterns = [
    url(r'^ws/chatbox/(?P<room_name>[^/]+)/$', consumers.ChatConsumer, name='chat'),
    #url(r'^ws/chatbox/(?P<room_name>[^/]+)//$', consumers.OnlineConsumer, name='status')
]