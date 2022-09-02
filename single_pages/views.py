from datetime import datetime
from django.shortcuts import redirect, render
from .models import Comment, Information, Profile
from diary.models import Post
from django.http import HttpResponseRedirect
import json

def landing(request):
    if request.user.is_authenticated:
        profile = Information.objects.last()
        postall=Post.objects.all().order_by('-created_at')
        img = Profile.objects.last()
        information = {'profile':profile, 'postall':postall, 'img':img}

        return render(request, 'single_pages/landing.html', information)
    else:
        return HttpResponseRedirect('login')

def login(request):
    return render(
        request,
        'single_pages/cover.html'
    )

def list(request):
    commentlist=Comment.objects.all().order_by('-created_at')
    data={'commentlist':commentlist}
    return render(request, 'single_pages/list.html',data)

def write(request):
    comment = Comment()
    comment.question=request.POST['question']
    comment.content=request.POST['content']
    comment.save()
    return HttpResponseRedirect('list')

def delete(request,id):
    comment = Comment.objects.filter(pk=id)
    if comment:
        comment.delete()
    return redirect('/list')

def information(request):
    information = Information()
    information.name = request.POST['name']
    information.email = request.POST['email']
    information.instagram = request.POST['instagram']
    information.mbti = request.POST['mbti']
    information.save()

    return redirect('/')
