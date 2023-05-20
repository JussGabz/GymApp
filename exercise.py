class Exercise:
    def __init__(self, name, desc, body_type):
        self.name = name
        self.desc = desc
        self.body_type = body_type

    def __str__(self):
        return f"Exercise: {self.name}"


class WorkOutPlan:
    def __init__(self, name, duration):
        self.name = name
        self.exercises = []
        self.duration = duration

    def workout_plan_name(self):
        """Return Workout Plan name"""
        return self.name

    def get_exercises(self):
        """Return exercises from workout plan"""
        return self.exercises

    def number_of_exercises(self):
        """Remove exercise from workout plan"""
        return len(self.exercises)

    def add_exercise(self, exercise):
        """Add exercise to workout plan"""
        self.exercises.append(exercise)
        return self.exercises

    def remove_exercise(self, exercise):
        """Remove exercise from workout plan"""
        if exercise in self.exercises:
            self.exercises.remove(exercise)
        return self.exercises
