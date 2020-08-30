from django.urls import path
from . import views

#add URL pattern to redirect to the list of posts when entering the website
#This URL pattern will match an empty string and the Django URL resolver will ignore the domain name that prefixes the full URL path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/', views.cvView, name='cv'),
]