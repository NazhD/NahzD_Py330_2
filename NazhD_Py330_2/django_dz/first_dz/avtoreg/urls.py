from django.urls import path
from . import views


urlpatterns = [
    path('reg', views.reg, name="reg"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('login', views.loginuser, name="loginuser"),
]