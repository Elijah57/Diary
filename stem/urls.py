from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="stem-bloghome"),
    path("info/", views.info, name = "info")
]