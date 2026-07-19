class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    #displaying info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Name: {self.age}")
        print(f"Name: {self.email}")
class Student(Person):
