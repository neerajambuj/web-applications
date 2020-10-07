from django.conf.urls import url, include
from django.urls import path
from chat import views
urlpatterns = [
    # Home Page
    path('',views.Run,name = 'Run'),
    ]
