from manager import StudentManager
from student import Student

def print_menu():
    print("\Student Record Manager")
    print("1. Add student")
    print("2. View all students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

def main():
    manager = StudentManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            department = input("Department: ")
            year = int(input("year: "))
            gpa = float(input("GPA: "))
            
            student = Student(student_id, name, department, year, gpa)
            manager.add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            students = manager.get_all_students()
            if not students:
                print("No students found.")
            else:
                for s in students:
                  print(
                    f"ID: {s.student_id}, "
                    f"Name: {s.name}, "
                    f"Dept: {s.department}, "
                    f"Year: {s.year}, "
                    f"GPA: {s.gpa}"
                  )
        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            student = manager.find_student_by_id(student_id)

            if student:
                student.name = input(f"Name ({student.name}): ") or student.name
                student.department = input(f"Department ({student.department}): ") or student.department
                student.year = int(input(f"Year ({student.year}): ") or student.year)
                student.gpa = float(input(f"GPA ({student.gpa}): ") or student.gpa)

                manager.save_to_file()
                print("Student updated succesfully.")
            else:
                print("Student not found.")
        elif choice =="4":
            student_id = int(input("Enter student ID to delete: "))
            student = manager.find_student_by_id(student_id)

            if student:
               manager.students.remove(student)
               manager.save_to_file()
               print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == "5":
            print("GoodBye.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
        
