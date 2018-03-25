from django.conf.urls import url
from basicApp import views

#templateURLS
app_name = 'basicApp'

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
]