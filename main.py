from student import Student
from teacher import Teacher

student1 = Student("Tayo", 12, "tayo@yahoo.com",74, "python", 2, 12)
student2 = Student("Bolu", 12, "tayo@yahoo.com", 4,"biology", 9,10)
teacher1 = Teacher("Mr. Smith", 40, "smith@gmail.com", "T001", "Mathematics", 50000)

student1.display_info()
print("-" * 100)
student2.display_info()
teacher1.display_info()

student1.get_grade()
print("-" * 100)
student2.get_grade()

student1.update_grade(75)
print("-" * 100)
student2.update_grade(80)

# STEP 7: Demonstrating Polymorphism here.


# Sample objects
student1 = Student(
    "Lawrence",
    25,
    "lawrence@gmail.com",
    "ST001",
    "Computer Science",
    "200 Level",
    85
)

teacher1 = Teacher(
    "Mr tunde",
    38,
    "tunde@gmail.com",
    "T001",
    "Python Programming",
    500000
)

# Demonstrate polymorphism
people = [student1, teacher1]

for person in people:
    person.perform_role()
