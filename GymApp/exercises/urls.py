from django.urls import path

from . import views
app_name = 'exercises'
urlpatterns = [
    path("", views.index, name='index'),
    path("exercise/<int:exercise_id>/", views.exercise_detail, name='exercise_detail'),
    path("<str:difficulty>/", views.exercise_difficulty),
]