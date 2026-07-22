from student import Student
from teacher import Teacher
from school_management import SchoolManagementSystem


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

# Step 8
# Create Student objects
student1 = Student("John Doe", 18, "Male", "STU001", "Computer Science", "100 level", 90)
student2 = Student("Mary Johnson", 19, "Female", "STU002", "Software Engineering", "100 level", 90)
student3 = Student("David Brown", 20, "Male", "STU003", "Information Technology", "100 level", 90)
student4 = Student("Grace Williams", 18, "Female", "STU004", "Cyber Security", "100 level", 90)
student5 = Student("Michael Smith", 21, "Male", "STU005", "Data Science", "100 level", 90)

# Create a Teacher object
teacher1 = Teacher(
    "Dr. Sarah Adams",
    42,
    "Female",
    "TCH001",
    "Computer Science",
    85000
)

# Store all student objects in a list
students = [student1, student2, student3, student4, student5]


#step 10
# Menu System

def exit_sms ():
    while True:
     choice = input("Yes / No : ")
     if choice.lower() == "yes" or choice.lower() == "y":
        print("Thank you for using the SMS (School Management System)!")
        return True
     elif choice.lower() == "no" or choice.lower() == "n":
        return False
     else:
        print("Enter Yes or No")

sms = SchoolManagementSystem()

while True:
    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
    print("\n1. Add Student")
    print("2. Add Teacher")
    print("3. Display All Students")
    print("4. Display All Teachers")
    print("5. Search Student")
    print("6. Update Grade")
    print("7. Exit")
    print("=" * 30)

    try:
        choice = int(input("Enter option 1-7: "))

        if choice < 1 or choice > 7:
            print("Please input numbers from 1-7")
            continue
    except ValueError:
        print("Please input numbers from 1-7")
        continue

    print("\n")

    if choice == 1:
        name = input("Enter student Name:")
        age = int(input("Enter student Age:"))
        email = input("Enter student Email:")
        student_id = input("Enter Student ID: ")
        course = input("Enter Student Course:")
        level = input("Enter Student Level:")
        grade =int(input("Enter Student Grade?:"))

        student = Student(
            name,
            age,
            email,
            student_id,
            course,
            level,
            grade,
        )
        sms.add_student(student)

    elif choice == 2:
        name = input("Enter Teacher Name:")
        age = int(input("Enter Teacher Age:"))
        email = input("Enter Teacher Email:")
        staff_id = input("Enter Staff ID:")
        subject = input("Enter Teacher's Subject:")
        salary = int(input("Enter Salary:"))

        teacher = Teacher(
            name, 
            age, 
            email, 
            staff_id, 
            subject, 
            salary,
        )
        sms.add_teacher(teacher)

    elif choice == 3:
        sms.display_all_students()
    
    elif choice == 4:
        sms.display_all_teachers()

    elif choice == 5:
        search_id = input("Enter Student ID: ")
        sms.find_student = student(search_id)
        if student:
            print("Student Found!")
            student.display_info()    
        else:
            print("Student not found")

    elif choice == "6":
        student_id = input("Enter Student ID: ")
        sms.find_student = student(student_id)
    
        if student:
          while True:
            new_grade = input("Enter new Grade: ")
            try:
              new_grade = float(new_grade)
              if 0 <= new_grade <= 100:
                student.gpa = new_grade
                print("Grade updated successfully.")
                break
              else:
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid numeric Grade.")
            else:
                print("Student not found.")
    
        elif choice == 7:
            print("Are you sure you want to exit?")
            if exit_sms():
                break
            else:
               print("Returning to the main menu...")
