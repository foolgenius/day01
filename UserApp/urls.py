from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^index/', views.index),
    #get_vcode_api
    url(r'^get_vcode/', views.get_vcode),
    #send_vcode
    url(r'^submit_vcode/', views.submit_vcode),
    # #get_profile
    # url(r'^get_profile/', views.get_profile),
    # #set_profile
    # url(r'^set_profile/', views.set_profile),
    # #upload_avtar
    # url(r'^upload_avatar/', views.upload_avatar),
]