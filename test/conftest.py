import pytest
from exercise import Exercise, WorkOutPlan


@pytest.fixture
def exercise_name():
    return "New Exercise"


@pytest.fixture
def exercise_desc():
    return "New Exercise Desc"


@pytest.fixture
def exercise_body_type():
    return "New Exercise Body Type"


@pytest.fixture
def workout_plan_name():
    return "New Workout Plan"


@pytest.fixture
def workout_plan_duration():
    return "12 Weeks"


@pytest.fixture
def new_exercise(exercise_name, exercise_desc, exercise_body_type):
    return Exercise(
        name=exercise_name, desc=exercise_desc, body_type=exercise_body_type
    )


@pytest.fixture
def workout_plan(workout_plan_name, workout_plan_duration):
    return WorkOutPlan(name=workout_plan_name, duration=workout_plan_duration)
