class SchoolManagementSystem:
    def __init__(self):
     self.students = []
     self.teachers = []

    def add_student(self, new_student):
       self.students.append(new_student)
       print(f"{new_student.name} has been added successfully.")

    def add_teacher(self, new_teacher):
       self.teachers.append(new_teacher)
       print(f"{new_teacher.name} has been added Successfully.")

    def display_all_students(self):
       if not self.students:
          print("No student Found.")
          return
       
       for student in self.students:
          student.display_info()
          print("-" * 30)
    
    def display_all_teachers(self): 
       if not self.teachers: 
          print("No teacher found.")
          return
       
       for teacher in self.teachers:
          teacher.display_info()
          print("-" * 30)

    def find_student(self, student_id):
     for student in self.students:
        if student.student_id.lower() == student_id.lower():
            return student
     return None