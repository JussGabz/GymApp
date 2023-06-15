from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Exercise


def index(request):
    # Latest 5 Exercises
    latest_exercises = Exercise.objects.order_by("-date_added")[:5]
    context = {"latest_exercises": latest_exercises}
    # output = ", ".join([ex.exercise_name for ex in latest_exercises])
    return render(request, "index.html", context)


def exercise_detail(request, exercise_id):

    exercise = get_object_or_404(Exercise, id=exercise_id)
    context = {"exercise": exercise}
    return render(request, "detail.html", context)

def exercise_difficulty(request, difficulty):
    exercises = Exercise.objects.filter(difficulty__iexact=difficulty)
    context = {
        "exercise_difficulty": difficulty,
        "exercises": exercises,
    }

    print(exercises)
    return render(request, "difficulty.html", context)


