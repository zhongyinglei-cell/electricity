# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import jiangpin,User
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def index(request):
    return render(request,'index.html',{})
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(username=username,password=password)
        if user_obj:
            print(username,password)
            auth.login(request,user_obj)
            return redirect('/')
        else:
            print('error')
            msg = '账号或密码不正确请重新输入'
            return render(request,'login.html',{'msg':msg})##return HttpResponse(json.dumps({'code': 403, 'status': '用户名密码错误！'}))
    return render(request,'login.html',{})

def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required(login_url='/error/')
def manage(request):
    return render(request,'manage.html',{})

def error(request):
    return render(request,'error.html',{})
@csrf_exempt
def home(request):
    # api_request = requests.get('https://api.github.com/users?since=0')
    # api = json.loads(api_request.content)
    return render(request,'home.html',{})

@login_required(login_url='/error/')
def choujiang(request):
    count = request.user.count
    if request.method == 'POST':
        jpdc = request.body
        name = json.loads(jpdc)['JP']
        print(name)
        count = request.user.count
        if len(name.split(',')) != 1:
            for i in name.split(','):
                us = request.user
                jp = jiangpin()
                jp.user = us
                jp.name = i
                jp.save()
                count -= 1
                us = User.objects.get(username=request.user.username)
                us.count = count
                us.save()
        else:
            us = request.user
            jp = jiangpin()
            jp.user = us
            jp.name = name
            jp.save()
            count -= 1
            us = User.objects.get(username=request.user.username)
            us.count = count
            us.save()
        count = request.user.count
        return render(request,'choujiang.html',{'count':count})
    else:
        return render(request, 'choujiang.html', {'count':count})
@csrf_exempt
def user(request):
    user = request.POST["user"]
    user_request = requests.get('https://api.github.com/' + user)
    api_user = json.loads(user_request.content)
    return render(request,'user.html',{'user':api_user})

def chongzhi(request):
    time = request.user.time
    if request.method == 'POST':
        time = request.user.time
        if time != 0:
            count_json = request.body
            count = json.loads(count_json)['count']
            us = User.objects.get(username=request.user.username)
            us.count += count
            us.time -= 1
            us.save()

        return render(request,'chongzhi.html',{'time':time})

    return render(request,'chongzhi.html',{"time":time})

