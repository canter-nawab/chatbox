from django.shortcuts import render
from .models import User, Message
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
import json
# Create your views here.

user_list = []

def new_user(request):
    try:
        current_user = User.objects.get(roll_no=request.POST['roll_no'])
    except User.DoesNotExist:
        current_user = None
    #message_list = Message.objects.all()
    if current_user:
        request.session['user'] = current_user.roll_no
        return render(request, 'chatbox/newconvo.html', {'user':current_user})
    #    return render(request, 'chatbox/chatspace.html', {'user':current_user, 'messages':message_list})
    #    return render(request, 'chatbox/conversations.html', {'user':current_user, 'conversations':conversations, 'ids':ids})
    else:   
        newuser = User.objects.create(user_name=request.POST['username'], roll_no=request.POST['roll_no'])
        request.session['user'] = newuser.roll_no
        conversations = None
        return render(request, 'chatbox/newconvo.html', {'user':newuser})
    #    return render(request, 'chatbox/chatspace.html', {'user':newuser, 'messages':message_list}, )
    #    return render(request, 'chatbox/conversations.html', {'user':newuser, 'conversations':conversations})

#def new_message(request):
#    if request.POST['message_box']:
#        newmessage = Message.objects.create(user=get_object_or_404(User, pk=request.session.get('user')), message=request.POST['message_box'])
#        request.session['user'] = newmessage.user.roll_no
#    message_list = Message.objects.all()
#    request.session.objects.all().reload()
#    return render(request, 'chatbox/chatspace.html', {'user':newmessage.user, 'messages':message_list,})

def new_convo(request):
    current_user = get_object_or_404(User, pk=request.session.get('user')).user_name
    return render(request, 'chatbox/newconvo.html', {'user': current_user})

def room(request, room_name):
    current_user = get_object_or_404(User, pk=request.session.get('user'))
    #convo_name = str(room_name)
    #second_member = convo_name - current_user.roll_no
    #if Conversation.objects.get(pk=room_name):
    #    current_convo = Conversation.objects.get(pk=room_name)
    #else:
    #    Conversation.objects.create(conversation_id=room_name, first_member=current_user, second_member=User.objects.get(roll_no=second_member))
    return render(request, 'chatbox/room.html', {'room_name_json':mark_safe(json.dumps(room_name)), 'user_ob':mark_safe(json.dumps(current_user.user_name)), 'user':current_user, 'user_list':user_list})