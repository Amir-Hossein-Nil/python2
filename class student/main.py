class student():
    def __int__(self, first_name, last_name, age, math_score, physics_score, python_score):
        self.first_name = input("first_name")
        self.last_name = input("last_name")
        self.age = input("age")
        self.math_score = input("math_score")
        self.physics_score = input("physics_score")
        self.python_score = input("python_score")

    def check_status(self):
        average_score = (int(self.math_score) + int(self.physics_score) + int(self.python_score)) / 3
        if average_score >= 17:
            print("accepted")
        elif average_score < 17:
            print("failed")


student1 = student()
student.check_status()
