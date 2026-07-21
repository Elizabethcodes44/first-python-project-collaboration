from person import Person
class Teacher(Person):

    def __init__(self, name, age, email, staff_id, subject, salary):
        super().__init__(name, age, email)
        self.staff_id = staff_id
        self.subject = subject
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Subject: {self.subject}")
        print(f"Salary: ₦{self.salary}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def assign_grade(self, student, new_grade):
        student.update_grade(new_grade)

    def perform_role(self):
        print(f"{self.name} is teaching and grading students.")
