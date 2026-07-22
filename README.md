# Student Management System

A command-line **Student Management System** built in Python using **Object-Oriented Programming**. This project was built for the CWP Python Expert Program, Week 1 (Day 2) assignment.

## Description

This program manages student and teacher records through a simple menu-driven interface. It demonstrates core OOP concepts by modeling a `Person` parent class, with `Student` and `Teacher` child classes that inherit from it. Users can view all students, search for a student by ID, check a student's result, update a student's grade (with validation), view teacher information, and see polymorphism in action.

Only the core project steps were implemented for this submission — no bonus features were added.

## Features

- View all students
- Search for a student by student ID
- View a student's result (grade interpreted through the grading system)
- Update a student's grade (with input validation)
- View teacher information
- Demonstrate polymorphism (`perform_role()` behaving differently for students vs. teachers)
- Menu-driven program that runs until the user chooses to exit
- Invalid menu input is handled gracefully

## Concepts Used

- Classes and objects
- Attributes and methods
- Constructors (`__init__`)
- Inheritance (`Student` and `Teacher` inherit from `Person`) using `super()`
- Encapsulation (private `__grade` attribute, accessed only through `get_grade()` and `update_grade()`)
- Polymorphism (`perform_role()` and `display_info()` overridden differently in each subclass)
- Lists, loops, functions, conditionals, user input, and error handling

## Folder Structure

```
student-management-system/
|-- main.py
|-- person.py
|-- student.py
|-- teacher.py
|-- README.md
|-- .gitignore
`-- screenshots/
    |-- main-menu.png
    `-- student-result.png
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/cwp-student-management-system.git
   cd cwp-student-management-system
   ```
2. Run the program:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to interact with the system.

## Sample Menu

```
STUDENT MANAGEMENT SYSTEM
1. View all students
2. Search for a student
3. View a student result
4. Update a student grade
5. View teacher information
6. Demonstrate polymorphism
7. Exit
```

## Sample Output / Screenshots

Screenshots of the program running are available in the `screenshots/` folder:
- `main-menu.png` — main menu running in the terminal
- `student-result.png` — student result / grade update output

## Author

Elizabeth, Lawrence and Faith
