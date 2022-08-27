from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('list', views.list, name='list'),
    path('write', views.write, name='write'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('information', views.information, name='information'),
    path('login', views.login,name='login'),
]