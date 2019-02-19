from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path('gogetthegood/', views.gogetthegood, name='index'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='index'),
    path('mycity/', views.mycity, name='index'),
    path('myeats/', views.myeats, name='index'),
]