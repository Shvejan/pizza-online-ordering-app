from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("loginUser/", views.loginUser, name="loginUser"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),
    path("signupUser/", views.signupUser, name="signupUser"),
    path("menu/", views.menu, name="menu"),
    path("viewCart/", views.viewCart, name="viewCart"),
    path("placeOrder/", views.placeOrder, name="placeOrder"),
    path("dataTester/", views.dataTester, name="dataTester"),






]
