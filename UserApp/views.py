import os

from django.core.cache import cache

from UserApp import logics
from UserApp.forms import UsermoduleForm, ProfileForm
from common import stat

from common import keys

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from UserApp.logics import send_vcode
from UserApp.models import User_module, Profile

from libs.qn_clound import upload_to_qn


def index(requeset):
    # a = cache.get(keys.VCODE % '15255665851')
    # uid = requeset.session.get('uid')
    # print(uid)
    x = requeset.path
    print(x)
    return HttpResponse('Successful!')

#get_vcode_api
def get_vcode(request):
    """ user get vocde    """
    #get args
    phonenum = request.GET.get('phonenum')

    result = send_vcode(phonenum)


    if result:
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': None})


#submit_vcode
def submit_vcode(request):
    """get user api info"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    cache_vcode = cache.get(keys.VCODE % phonenum)
    print(phonenum)
    print('===========')
    print(vcode)
    print('===========')
    print(cache_vcode)
    if vcode and cache_vcode and cache_vcode == vcode:
        try:
            user = User_module.objects.get(u_phonenum=phonenum)
        except User_module.DoesNotExist:
            user = User_module.objects.create(u_phonenum=phonenum, u_name=phonenum)

        request.session['uid'] = user.id
        print(request.session['uid'])
        return JsonResponse({'code':0, 'data':user.to_dict()})
    else:
        return JsonResponse({'code':1001, 'data': None})


def get_profile(request):
    uid = request.session['uid']
    profile, _ = Profile.objects.get_or_create(id=uid)

    return JsonResponse({'code': stat.OK, 'data': profile.to_dict()})

def set_profile(request):
    user_form = UsermoduleForm(request.POST)
    if not user_form.is_valid():
        return JsonResponse({'code':stat.USERMODULE_FORM_ERR, 'data':None})

    profile_form = ProfileForm(request.POST)
    if not profile_form.is_valid():
        return JsonResponse({'code':stat.PROFILE_FORM_ERR,'data':None} )


def upload_avatar(request):
    uid = request.session['uid']
    avatar_file = request.FILES.get('avatar')

    avatar_name, avatar_path = logics.save_upload_avatar(uid, avatar_file)

    avatar_url = upload_to_qn(avatar_name, avatar_path)

    user = User_module.objects.create(id=uid)
    user.u_avatar = avatar_url
    user.save()

    os.remove(avatar_path)

    return JsonResponse({'code':0, 'data':None})