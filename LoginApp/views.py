# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from LoginApp.models import User


def index(request):
    return render(request, 'test.html')


def register_page(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        user = User()
        user.u_name = request.POST.get('name')
        user.u_password = request.POST.get('password')
        user.u_sex = request.POST.get('sex')
        user.u_birthday = request.POST.get('birthday')
        user.u_phonenum = request.POST.get('phonenum')
        user.u_location = request.POST.get('location')
        user.u_active = True
        user.save()

        return render(request, 'go_login_page.html')


@csrf_exempt
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.filter(u_name=name)
        password = User.objects.filter(u_password=password)

        data = {
            'status':'201',
            'msg':'no found user, go to register.'
        }

        if not user.count():
            return JsonResponse(data=data)
        else:
            if not password.count():
                data['status'] = '202'
                data['msg'] = 'password is False'
                return JsonResponse(data=data)
            else:
                data['status'] = '200'
                data['msg'] = 'welcom login'
                return JsonResponse(data=data)

class Abc(object):

    def __next__(self):
        pass

    def __iter__(self):
        pass




