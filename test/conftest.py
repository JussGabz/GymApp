import pytest
from exercise import Exercise, WorkOutPlan

@pytest.fixture
def exercise_name():
    return 'Exercise Name'

@pytest.fixture
def exercise_desc():
    return 'Exercise Desc'

@pytest.fixture
def exercise_body_type():
    return 'Exercise Body Type'

@pytest.fixture
def first_exercise():
    exercise = Exercise(
        name='First Exercise',
        desc='First Exercise Desc',
        body_type='First Exercise Body Type'
    )
    return exercise

@pytest.fixture
def second_exercise():
    return Exercise(
        name='Second Exercise',
        desc='Second Exercise Desc',
        body_type='Second Exercise Body Type'
    )

@pytest.fixture
def new_exercise():
    return Exercise(
        name='New Exercise',
        desc='New Exercise Desc',
        body_type='New Exercise Body Type'
    )



@pytest.fixture
def workout_plan(first_exercise, second_exercise):
    return WorkOutPlan(
        name='New Work Out Plan',
        exercises=[first_exercise, second_exercise],
        duration='12 Weeks'
    )

