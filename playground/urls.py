from django.urls import path
from . import views

#urlconfiguration
#create a path and request handler function
#use  the path() function to create a urlpattern object
urlpatterns = [
    path("", views.home, name="home"),
    path("info/", views.tell_info),
    path("about/", views.About),
    path("register/", views.Register, name="register"),
    path("register/add/", views.add_to_db, name="add" )
]