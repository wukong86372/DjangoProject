from django.shortcuts import render,redirect
from .models import Message,Like

# Create your views here.
def index(request):
    messages = Message.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        message = Message()
        message.text = text
        message.username = request.user.username
        message.title = title
        message.dislike_num = 0
        message.like_num = 0
        message.save()
        return redirect('board:index')
    return render(request,'board/index.html',{'messages':messages})


def like(request):
    if request.method == 'POST':
        msg_id = request.POST.get('mes_id')
        user_id = request.user.id
        likes = Like.objects.filter(person_id=user_id,message_id=msg_id)
        liked = False
        disliked = False
        for like in likes:
            if like.person_id == user_id and like.like_type == True:
                liked = True
            if like.person_id == user_id and like.like_type == False:
                disliked = True
        message = Message.objects.get(id=msg_id)
        if 'dislike' in request.POST and disliked == False:
            message.dislike_num = message.dislike_num + 1
            like = Like()
            like.person_id = user_id
            like.message_id = msg_id
            like.like_type = False
            like.save()
            message.save()
        elif 'like' in request.POST and liked == False:
            message.like_num = message.like_num + 1
            like = Like()
            like.person_id = user_id
            like.message_id = msg_id
            like.like_type = True
            like.save()
            message.save()
    return redirect('board:index')


