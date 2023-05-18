

def test_exercise(first_exercise):
    assert first_exercise.name == "First Exercise"


def test_list_exercises(first_exercise, second_exercise, workout_plan):
    

    assert workout_plan.list_of_exercises() == [
        {
            'name': first_exercise.name,
            'description': first_exercise.desc,
            'body type': first_exercise.body_type
        },
        {
            'name': second_exercise.name,
            'description': second_exercise.desc,
            'body type': second_exercise.body_type
        }
    ]

def test_workout_plan_name(workout_plan):
    assert workout_plan.workout_plan_name() == 'New Work Out Plan'

def test_number_of_exercises(workout_plan):
    assert workout_plan.number_of_exercises() == 2

def test_add_exercise(workout_plan, new_exercise):

    exercises = workout_plan.list_of_exercises()

    new_exercises = exercises.append(vars(new_exercise))

    print(exercises)

    print(exercises.append(vars(new_exercise)))
    
    assert workout_plan.add_exercise(new_exercise) == new_exercises
    

def test_remove_exercise():
    pass




