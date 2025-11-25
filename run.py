from project1 import students

if __name__ == "__main__":
    username = input("Enter the username: ").lower()
    password = input("Enter the password: ")
    student = students.StudentManagement(username, password)
    student.validation()