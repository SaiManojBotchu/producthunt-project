from django.urls import path,include
from . import views

urlpatterns = [

    path('sai',views.sai,name='sai'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
