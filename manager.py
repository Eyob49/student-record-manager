import json
from student import Student

class StudentManager:
    def __init__(self, data_file = "data.json"):
        self.data_file = data_file
        self.students = []
        self.load_from_file()

    def add_student(self, student):
        self.students.append(student)
        self.save_to_file()

    def get_all_students(self):
        return self.students
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
            return None
        
    def save_to_file(self):
        with open(self.data_file, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)
    def load_from_file(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []


if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student(Student(1, "Test User", "CS", 2, 3.5))
    print(len(manager.get_all_students()))


                      