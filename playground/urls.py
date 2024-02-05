from django.urls import path
from playground import views

urlpatterns = [
    path("hello/", views.sayHello),
    path("img/", views.sendIMG),
    path("json/", views.sendJSON),
    path("", views.sendHTML),
    path("html/", views.sendHTML),

    path("crud/", views.handleCrud),
    path("set_cookie/", views.set_cookie),
    path("get_cookie/", views.get_cookie),

]

