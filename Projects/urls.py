from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    # path('about/', views.index, name='about'),
    # path('contact/', views.index, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog-black/', views.blog_black, name='blog-black'),
    path('blog-details/', views.index, name='blog-details'),
    path('blog-details-black/', views.index, name='blog-details-black'),
    path('index-1/', views.index_one, name='index-1'),
    path('index-2/', views.index_two, name='index-2'),
    path('index-3/', views.index_three, name='index-3'),
    path('index-4/', views.index_four, name='index-4'),
    path('index-5/', views.index_five, name='index-5'),
    path('index-6/', views.index_six, name='index-6'),
    path('index-8/', views.index_eight, name='index-8'),
    path('index-9/', views.index_nine, name='index-9'),
    path('index-10/', views.index_ten, name='index-10'),
    path('ct_msg_send/', views.ct_msg_send, name='ct_msg_send'),
]
