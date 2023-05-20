def test_exercise(new_exercise):
    assert new_exercise.name == "New Exercise"


def test_workout_plan_name(workout_plan):
    assert workout_plan.workout_plan_name() == "New Workout Plan"


def test_number_of_exercises(workout_plan, new_exercise):
    assert workout_plan.number_of_exercises() == 0

    workout_plan.add_exercise(new_exercise)
    assert workout_plan.number_of_exercises() == 1


def test_add_exercise(workout_plan, new_exercise):
    # Add Exercise
    workout_plan.add_exercise(new_exercise)
    assert workout_plan.get_exercises() == [
        new_exercise
    ], "Exercises list not updated as expected"


def test_remove_exercise(workout_plan, new_exercise):
    # Add exercise to workout plan
    workout_plan.add_exercise(new_exercise)

    workout_plan.remove_exercise(new_exercise)
    assert workout_plan.get_exercises() == []
