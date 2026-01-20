class Student:
    def __init__(self, student_id, name, department, year, gpa):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.year = year
        self.gpa = gpa

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "year": self.year,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["department"],
            data["year"],
            data["gpa"]
        )
    
if __name__ == "__main__":
    s = Student(1, "Test User", "CS", 2, 3.5)
    print(s.to_dict())