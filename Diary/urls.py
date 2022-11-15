from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="diary-home"),
    path("write/", views.create_diary, name="create"),
    path("read/<int:id>/", views.read, name="read"),
    path("edit/<int:id>/", views.edits, name="edit"),
    path("delete/<int:id>", views.dele, name="delete"),
    path("register/", views.register_user, name="diary-users-register")
]