from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:exercise_id>/", views.exercise_detail),
    path("<str:difficulty>/", views.exercise_difficulty),
]