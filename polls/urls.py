from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #ex polls/5
    path("<int:id>/", views.details, name="details"),
    #ex polls/5/result
    path("<int:id>/result/", views.result, name="result"),
    #ex polls/5/vote
    path("<int:id>/vote/", views.vote, name="vote")
]