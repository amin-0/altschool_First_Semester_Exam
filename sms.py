
class Person:
    def __init__(self, name: str, id_number: int) -> None:
        self.name = name
        self.id_number = id_number
    
    def __str__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}"

class Student(Person):
    def __init__(self, name: str, id_number:int, major:str) -> None:
        super().__init__(name, id_number)
        self.major = major
    
    def __str__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}, major: {self.major}"

class Instructor(Person):
    def __init__(self, name:str, id_number:int, department:str) -> None:
        super().__init__(name, id_number)
        self.department = department
    
    def __str__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}, department: {self.department}"

class Course:
    def __init__(self, course_name:str, course_id:int, enrolled_students:list[Student] = []) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = enrolled_students
    
    def __str__(self) -> str:
        return f"course name: {self.course_name}, course_id: {self.course_id}"

class Enrollment:
    def __init__(self, student: Student, course: Course, grade:int = None) -> None:
        self.student = student
        self.course = course
        self.grade = grade
    
    def __str__(self) -> str:
        return f"name: {self.student.name} is enrolled in {self.course.course_name}"

class StudentManagementSystem:
    def __init__(self) -> None:
        self.students: list[Student] = []
        self.courses: list[Course] = []
        self.instructors: list[Instructor] = []
        self.enrollments: list[Enrollment] = []

