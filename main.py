from student import Student

student1 = Student("Tayo", 12, "tayo@yahoo.com",74, "python", 2, 12)
student2 = Student("Bolu", 12, "tayo@yahoo.com", 4,"biology", 9,10)

student1.display_info()
print("-" * 100)
student2.display_info()

student1.get_grade()
print("-" * 100)
student2.get_grade()

student1.update_grade(75)
print("-" * 100)
student2.update_grade(80)
