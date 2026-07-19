class Student(Person):
    def __init__(self, name, age, email, student_Id, course, level, grade):
        super().__init__(name, age, email)
        self.student_Id = student_Id
        self.course = course
        self.level = level
        self.grade = grade
    
    def display_info(self):
        print(f"My name is {self.name}.I am {self.age}.My email address is {self.email}.My student Id is {self.student_Id}.I am studying {self.course}.I am in level {self.level}.I am in grade {self.grade}")

student1 = Student("Tayo", 12, "tayo@yahoo.com",74, "python", 2, 12)
student2 = Student("Bolu", 12, "tayo@yahoo.com", 4,"biology", 9,10)

student1.display_info()
student2.display_info()