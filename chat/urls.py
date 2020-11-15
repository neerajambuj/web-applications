from django.conf.urls import url, include
from django.urls import path
from . import views
urlpatterns = [
    # Home Page
    url(r'^launch/$',views.launch,name = 'launch'),
    #url(r'',views.homepage,name = 'homepage'),
    path('chat',views.StartBot,name = 'StartBot'),
    #path('launch',views.launch,name = 'launch'),
    #path('')
    ]
