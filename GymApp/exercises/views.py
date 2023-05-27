from django.http import HttpResponse
from django.template import loader
from .models import Exercise


def index(request):
    # Latest 5 Exercises
    latest_exercises = Exercise.objects.order_by("-date_added")[:5]

    template = loader.get_template("index.html")
    context = {"latest_exercises": latest_exercises}

    loader.get_template("index.html")


    # output = ", ".join([ex.exercise_name for ex in latest_exercises])

    return HttpResponse(template.render(context, request))

def exercise_detail(request, exercise_id):
    response = "This is the exercise detail for exercise: %s"
    return HttpResponse(response % exercise_id)

def exercise_difficulty(request, difficulty):
    response = "This is the %s exercises"
    return HttpResponse(response % difficulty)


