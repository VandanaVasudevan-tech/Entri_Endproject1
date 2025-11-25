# Entri_Endproject1
A fully functional Command-Line Student Management System built using Python. This application allows you to securely manage student records with features such as adding, viewing, updating, deleting, searching, and ranking students.

Student data is stored in a JSON file and loaded safely using robust file-handling methods.
User login is validated through a config.ini file.

📌 Features
🔐 User Authentication
- Username and password read from config.ini.
- Prevents unauthorized access.

🎓 Student Management Operations
- Add Student
- View Students
- Update Students
- Delete Students
- Search by Name / Department
- Display Top Student (by marks)

📁 File Handling
- Safe JSON loading using:

  Missing file → returns empty dict
  Invalid JSON → returns empty dict
- Auto student ID generation
- Timestamp stored for each entry

🏗️ Project Structure

project1/
│── .gitignore
│── config.ini
│── functions.py
│── README.md
│── run.py
└── students.py


⚙️ Configuration File (config.ini)

    [login]
    username = admin123
    password = Pass@1234
    
▶️ How to Run

1. Clone the repository:
   git clone <your-repo-url>
2. python run.py
3. Enter credentials from config.ini
4. Use the menu options to manage students:
   ----- Student Management Menu -----
          1. Add Student
          2. View Students
          3. Update Student
          4. Delete Student
          5. Search Student
          6. Top Student
          7. Exit

🧪 Example Data Format (students.txt)
{
    "101": {
        "Student_ID": 1,
        "Name": "Vandana",
        "Age": 20,
        "Department": "CSE",
        "Marks": 92,
        "Created_at": "2025-11-25 10:30:45"
    }
}

