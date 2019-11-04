from django.conf.urls import url

from LoginApp import views

urlpatterns = [
    url(r'^index/', views.index),
    #register_page
    url(r'^register_page/', views.register_page),
    #login_page
    url(r'^login_page/', views.login_page)
]