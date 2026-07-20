from person import Person

class Student(Person):
    def __init__(self, name, age, email, student_Id, course, level, grade):
        super().__init__(name, age, email)
        self.student_Id = student_Id
        self.course = course
        self.level = level
        self.__grade = grade
    
    def display_info(self):
        print(f"My name is {self.name}.I am {self.age}.My email address is {self.email}.My student Id is {self.student_Id}.I am studying {self.course}.I am in level {self.level}.I am in grade {self.__grade}")
    
    def study(self):
        print(f"I am studying {self.course}")

    def get_grade(self):
       return self.__grade

    
    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print("Grade updated successfully."
                  )
        else:
            print("Invalid grade. Enter a value from 0 to 100")

    def check_result(self):
        pass

    def perform_role(self):
        pass

