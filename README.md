# Student Result Manager CLI

---

## Overview
This is a **Python command-line student result manager**. Users can add students, record subject grades, view individual student results, and list all registered students. The project demonstrates basic Python programming concepts and interactive CLI design.

---

## Features
- Add new students with unique student IDs  
- Record subject grades for existing students  
- View individual student records with grades  
- View all registered students  
- Input validation for existing student IDs  
- Interactive menu loop until exit  

---

## How to Run
1. Open `student_result_manager.py` in a Python environment that supports input and print (e.g., Pyto, Carnets, VS Code, or any desktop Python IDE).  
2. Run the script:

```bash
python student_result_manager.py
```
## Example Interaction                
```
--- Student Result Manager ---
1. Add student
2. Add grade
3. View student
4. View all students
5. Exit
Enter choice: 1
Enter student ID: 123
Enter student name: Labib
Student Labib added successfully!

--- Student Result Manager ---
1. Add student
2. Add grade
3. View student
4. View all students
5. Exit
Enter choice: 2
Enter student ID: 123
Enter subject: Math
Enter grade: 95
Grade added for Labib

--- Student Result Manager ---
1. Add student
2. Add grade
3. View student
4. View all students
5. Exit
Enter choice: 3
Enter student ID: 123

Name: Labib
Grades:
  Math: 95
```
## Skills Demonstrated                  
   - Python fundamentals: functions,  loops, dictionaries
   - CLI design and user input handling
   - Dynamic data management and record keeping
   - Menu-driven interactive programs

## License                            
     This project is licensed under the MIT License 
