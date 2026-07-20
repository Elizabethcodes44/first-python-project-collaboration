from person import Person

class Student(Person):
    def __init__(self, name, age, email, student_Id, course, level, grade):
        super().__init__(name, age, email)
        self.student_Id = student_Id
        self.course = course
        self.level = level
        self.grade = grade
    
    def display_info(self):
        print(f"My name is {self.name}.I am {self.age}.My email address is {self.email}.My student Id is {self.student_Id}.I am studying {self.course}.I am in level {self.level}.I am in grade {self.grade}")

