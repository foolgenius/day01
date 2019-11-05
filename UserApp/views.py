from django.core.cache import cache

from common import stat

from common import keys

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from UserApp.logics import send_vcode
from UserApp.models import User_module


def index(requeset):
    a = cache.get(keys.VCODE % '15255665851')
    print(a)
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
            return JsonResponse({'code':0, 'data':user.to_dict()})
    else:
        return JsonResponse({'code':1001, 'data': None})



#
# def get_profile(request):
#     """get profile"""
#     #get current user
#     uid = request.session['uid']
#     # try:
#     #     profile = Profile.objects.get(id=uid)
#     # except Profile.DoesNotexist:
#     #     profile.objects.create(id = uid)
#
#     profile, _ = Profile.objects.get_or_create(id=uid)
#
#     return JsonResponse({'code': stat.OK, 'data':profile.to_dict()})


# def set_profile(request):
#     u_name = None
#     u_sex = None
#     u_birthday = None
#     u_location = None
#     return None
#
#
# def upload_avatar(request):
#     return None