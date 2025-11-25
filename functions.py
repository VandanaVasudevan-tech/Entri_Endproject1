import json
import os.path
from datetime import datetime


def loadfile(filename):
    """
    Safely loads and returns JSON data from the given file.

    - If the file does not exist, returns an empty dictionary.
    - If the file exists but contains invalid JSON, returns an empty dictionary.
    - Handles unexpected errors gracefully and prevents program crashes.
    Returns:
        dict: Parsed JSON data or an empty dictionary if loading fails.
    """
    try:
        if not os.path.exists(filename):
            return {}
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    except Exception as e:
        print("Unexpected error while loading file:", e)
        return {}


def write_to_file(students, filename):
    """This Function is used to write and save to a file ."""
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4)
    except Exception as e:
        print("Error:", e)


def generate_student_id(student_details):
    """This Function is used to Auto-generate student ID ."""
    if not student_details:
        return 1
    ids = [student["Student_ID"] for student in student_details.values()]
    return max(ids) + 1


def add_student(student_details, filename):
    """This Function is used to add students."""
    try:
        student_ID = generate_student_id(student_details)
        name = input("Enter firstname: ")
        roll_number = int(input("Enter Roll Number: "))
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        marks = int(input("Enter Marks: "))
        student_data = {
            "Student_ID": student_ID,
            "Name": name,
            "Age": age,
            "Department": department,
            "Marks": marks,
            "Created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        student_details[roll_number] = student_data
        write_to_file(student_details, filename)
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)


def view_student(filename):
    """This Function is used to display all student data in a user-friendly format"""
    try:
        students = loadfile(filename)
        for key, details in students.items():
            print(f"Roll Number: {key}")
            print(f"  Student_ID: {details['Student_ID']}")
            print(f"  Name      : {details['Name']}")
            print(f"  Age       : {details['Age']}")
            print(f"  Department: {details['Department']}")
            print(f"  Marks     : {details['Marks']}")
            print(f"  Time of Entry : {details['Created_at']}")
            print("-" * 40)
    except Exception as e:
        print("Error:", e)


def update_student(filename, roll_number):
    """This Function is used to allow editing any field based on Roll Number."""
    try:
        students = loadfile(filename)
        if roll_number not in students:
            print("Roll number not found!")
            return
        value = students[roll_number]
        print(f"  Name      : {value['Name']}")
        print(f"  Age       : {value['Age']}")
        print(f"  Department: {value['Department']}")
        print(f"  Marks     : {value['Marks']}")
        print(f"__" * 10)
        print("What you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Department")
        print("4. Marks")
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            students[roll_number]["Name"] = input("Enter the new name: ")
        elif choice == 2:
            students[roll_number]["Age"] = input("Enter the new age: ")
        elif choice == 3:
            students[roll_number]["Department"] = input("Enter the new Department: ")
        elif choice == 4:
            students[roll_number]["Marks"] = input("Enter the new Marks: ")
        else:
            print("choose the correct option!")
            return
        write_to_file(students, filename)
        print(" Updated Successfully !!")
    except Exception as e:
        print("Error:", e)


def delete_student(filename, roll_number):
    """This Function is used to remove a student based on Roll Number"""
    try:
        students = loadfile(filename)
        if roll_number not in students:
            print("Roll number not found!")
            return
        del students[roll_number]
        write_to_file(students, filename)
        print(" Deleted Successfully !!")
    except Exception as e:
        print("Error:", e)


def search_student(filename, s_name, s_department):
    """This Function is used to search student by name or department"""
    try:
        students = loadfile(filename)
        found = False
        for key, value in students.items():
            match_name = (s_name == "" or value["Name"].lower() == s_name)
            match_dept = (s_department == "" or value["Department"].lower() == s_department)
            if match_name and match_dept:
                found = True
                print(f"Roll Number: {key}")
                print(f"  Name      : {value['Name']}")
                print(f"  Age       : {value['Age']}")
                print(f"  Department: {value['Department']}")
                print(f"  Marks     : {value['Marks']}")
                print("-" * 40)
        if not found:
            print(f" Oops!! No result. Try again with existing name / department !!")
    except Exception as e:
        print("Error:", e)


def top_student(filename):
    """This Function is used to find the topper based on marks"""
    try:
        students = loadfile(filename)
        if not students:
            print("No students found!")
            return
        topper_roll = max(students, key=lambda r: students[r]["Marks"])
        topper = students[topper_roll]
        print("\n----- Top Performing Student -----")
        print(f"Roll Number: {topper_roll}")
        print(f"Student_ID: {topper['Student_ID']}")
        print(f"Name      : {topper['Name']}")
        print(f"Age       : {topper['Age']}")
        print(f"Department: {topper['Department']}")
        print(f"Marks     : {topper['Marks']}")
        print("----------------------------------")
    except Exception as e:
        print("Error:", e)

