
class Person:
    def __init__(self, name: str, id_number: str) -> None:
        self.name = name
        self.id_number = id_number
    
    def __str__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}"

class Student(Person):
    def __init__(self, name: str, id_number:str, major:str) -> None:
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
    
    def __str__(self) -> str:
        return f"This is a student management system"
    
    def add_student(self, student : Student):
        self.students.append(student)

    def remove_student(self, student_id : str):
        #Add a try catch to check if the id is in the sms
        student = [student for student in self.students if student.id_number == student_id ][0]
        self.students.remove(student)
    
    def get_students(self) -> list[Student] :
        return [student.name for student in self.students]

    def update_students(self, id : str, updated_name : str, updated_major : str):
        student = [student for student in self.students if student.id_number == id ][0]
        student.name = updated_name
        student.major = updated_major
    
    def update_instructor(self, id : str, updated_name : str, updated_department : str):
        instructor = [instructor for instructor in self.instructors if instructor.id_number == id ][0]
        instructor.name = updated_name
        instructor.department = updated_department
        
    def get_instructors(self) -> list[Instructor] :
        return [instructor.name for instructor in self.instructors]
    
    def add_course(self, course : Course):
        self.course.append(course)

    def remove_course(self, course_id : str):
        course = [course for course in self.course if course.id_number == course_id ][0]
        self.course.remove(course)
    
    def update_course(self, id : str, updated_name : str, updated_major : str):
        student = [student for student in self.students if student.id_number == id ][0]
        student.name = updated_name
        student.major = updated_major

    def add_course():
        pass

    def remove_course():
        pass

    def update_course():
        pass