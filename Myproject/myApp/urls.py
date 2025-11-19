from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.Home,name='home'),
    #path('create/',views.stdForm,name='stdForm'),
    path('addstd/',views.registerstudent, name='register_std'),
    path('addstd', views.registerstudent,name="addstd"),
    path('fetch_std/',views.retrievestd,name='fetch_std'),
    path('updateStd/<int:pk>',views.updateStd,name='updateStd'),
    path('deleteStd/<int:pk>',views.deleteStd,name='deleteStd'),
    path('signup/',views.userRegistration,name="signup"),


    ]

