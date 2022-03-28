from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from EventManage import views

import EventManage

urlpatterns = [
    path('',views.index,name='index'),
    path('eventregistration', views.eventRegistration, name='event')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)