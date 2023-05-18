
class Exercise:
    def __init__(self, name, desc, body_type):
        self.name = name
        self.desc = desc
        self.body_type = body_type


class WorkOutPlan:
    def __init__(self, name, exercises, duration):
        self.name = name
        self.exercises = exercises
        self.duration = duration

    def list_of_exercises(self):
        exercise_list = []
        exercises = self.exercises

        for exercise in exercises:
            exercise_list.append(
                {
                    'name': exercise.name,
                    'description': exercise.desc,
                    'body type': exercise.body_type
                }
            )
        return exercise_list

    def workout_plan_name(self):
        return self.name

    def number_of_exercises(self): 
        return len(self.exercises)
    

    def add_exercise(self, exercise):
        new_exercise_list = []
        exercise_list = self.exercises
        for existing_exercise in exercise_list:
            new_exercise_list.append(
                {
                    'name': existing_exercise.name,
                    'description': existing_exercise.desc,
                    'body type': existing_exercise.body_type
                }
            )
        
        for new_exercise in [exercise]:
            new_exercise_list.append(
                {
                    'name': new_exercise.name,
                    'description': new_exercise.desc,
                    'body type': new_exercise.body_type
                }
            )
        return new_exercise_list

    def remove_exercise(self, exercise):
        if exercise in self.exercises:
            self.exercises.remove(exercise)
        return self.exercises