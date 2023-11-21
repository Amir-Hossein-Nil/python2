class student():
    def __int__(self, first_name, last_name, age, math_score, physics_score, python_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.math_score = math_score
        self.physics_score = physics_score
        self.python_score = python_score

    def check_status(self):
        average_score = (self.math_score + self.physics_score + self.python_score) / 3
        if average_score >= 17 :
            print("accepted")
        elif average_score < 17:
            print("failed")