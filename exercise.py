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
        return self.name

    def get_exercises(self):
        return self.exercises

    def number_of_exercises(self):
        return len(self.exercises)

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        return self.exercises

    def remove_exercise(self, exercise):
        """Remove exercise from workout plan"""
        if exercise in self.exercises:
            self.exercises.remove(exercise)
        return self.exercises
