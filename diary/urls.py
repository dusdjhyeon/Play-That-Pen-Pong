from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>/', views.delete_post, name='post_delete'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('guest_book', views.guest_book, name='guest_book'),
    path('guest_write', views.guest_write, name='guest_write'),
    path('guest_delete/<int:pk>/', views.guest_delete, name='guest_delete'),
    path('avatar', views.avatar),
    path('avatar_profile',views.avatar_profile, name='avatar_profile')
]