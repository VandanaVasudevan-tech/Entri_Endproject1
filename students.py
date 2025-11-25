import functions
import configparser


class StudentManagement:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def validation(self):
        try:
            if (self.config["login"]["username"] == self.username and
                    self.config["login"]["password"] == self.password):
                print("Login Successful!!")
                filename = "../students.txt"
                student_details = functions.loadfile(filename)
                while True:
                    print("\n----- Student Management Menu -----")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Update Student")
                    print("4. Delete Student")
                    print("5. Search Student")
                    print("6. Top Student")
                    print("7. Exit")

                    choice = int(input("Enter your Choice: "))
                    if choice == 1:
                        functions.add_student(student_details, filename)
                    elif choice == 2:
                        functions.view_student(filename)
                    elif choice == 3:
                        roll_number = input("Enter Student Roll Number: ")
                        functions.update_student(filename, roll_number)
                    elif choice == 4:
                        roll_number = input("Enter Student Roll Number: ")
                        functions.delete_student(filename, roll_number)
                    elif choice == 5:
                        name = input("Enter Student Name (or press Enter to skip): ").lower()
                        department = input("Enter Department (or press Enter to skip): ").lower()
                        functions.search_student(filename, name, department)
                    elif choice == 6:
                        functions.top_student(filename)
                    elif choice == 7:
                        print("Exiting...")
                        break
            else:
                print("Enter Valid Credentials!!")
        except Exception as e:
            print("Error:", e)

