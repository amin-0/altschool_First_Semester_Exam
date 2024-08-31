
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
    def __repr__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}, major: {self.major}"

class Instructor(Person):
    def __init__(self, name:str, id_number:int, department:str) -> None:
        super().__init__(name, id_number)
        self.department = department
    
    def __str__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}, department: {self.department}"
    def __repr__(self) -> str:
        return f"name: {self.name}, id_number: {self.id_number}, department: {self.department}"

class Course:
    def __init__(self, course_name:str, course_id:int, enrolled_students:list[Student] = []) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = enrolled_students
    
    def add_student(self, student: Student) -> list[Student]:
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
    
    def remove_student(self, student: Student) -> list[Student]:
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
    
    def __str__(self) -> str:
        return f"course name: {self.course_name}, course_id: {self.course_id}"
    def __repr__(self) -> str:
        return f"course name: {self.course_name}, course_id: {self.course_id}"

class Enrollment:
    def __init__(self, student: Student, course: Course, grade:int = None) -> None:
        self.student = student
        self.course = course
        self.grade = grade
    
    def assign_grade(self, grade: int):
        self.grade = grade

    def __str__(self) -> str:
        return f"name: {self.student.name} is enrolled in {self.course.course_name} and has a grade of {self.grade}"
    def __repr__(self) -> str:
        return f"name: {self.student.name} is enrolled in {self.course.course_name} and has a grade of {self.grade}"

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
            self.students = [student for student in self.students if student.id_number != student_id ]
        
    
    def get_students(self) -> list[Student] :
        return [student for student in self.students]

    def update_students(self, id : str, updated_name : str = None, updated_major : str = None):
        for student in self.students:
            if student.id_number == id:
                if updated_name:
                    student.name = updated_name
                if updated_major:
                    student.major = updated_major
    
    def add_instructor(self, instructor : Instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, id : str):
            self.instructors = [instructor for instructor in self.instructors if instructor.id_number != id ]
     
    def update_instructors(self, id : str, updated_name : str = None, updated_department : str = None):
        for instructor in self.instructors:
            if instructor.id_number == id:
                if updated_name:
                    instructor.name = updated_name
                if updated_department:
                    instructor.department = updated_department

    def get_instructors(self) -> list[Instructor] :
        return [instructor for instructor in self.instructors]
    
    def add_course(self, course : Course):
        self.courses.append(course)

    def remove_course(self, course_id : str):
        self.courses = [course for course in self.courses if course.course_id != course_id ]
    
    def update_course(self, id : str, updated_course_name : str):
        for course in self.courses:
            if course.course_id == id:
                course.course_name = updated_course_name
    
    def get_courses(self) -> list[Course] :
        return [course for course in self.courses]
    
    def enroll_student_in_course(self, student_id: str, course_id: str):
        print("Attempting enrollment")
        student_list = [student for student in self.students if student.id_number == student_id]
        student = student_list[0] if student_list else None

        course_list = [course for course in self.courses if course.course_id == course_id]
        course = course_list[0] if course_list else None

        if student and course:
            course.add_student(student=student)
            new_enrollment = Enrollment(student=student, course=course)
            print(new_enrollment)
            self.enrollments.append(new_enrollment)
            print("Enrollment successful")
        else:
            print("Enrollment unsuccessful")
        
    def get_enrollment(self) -> list[Enrollment] :
        return self.enrollments

    def assign_student_grade_for_course(self, student_id: str, course_id:str, grade:int):
        enrollment_list = [enrollment for enrollment in self.enrollments 
                           if (enrollment.student.id_number == student_id) 
                           and(enrollment.course.course_id == course_id)]
        enrollment = enrollment_list[0] if enrollment_list else None

        if enrollment:
            enrollment.assign_grade(grade=grade)
    
    def retrieve_student_in_course(self, course_id: str ):
        course_list = [course for course in self.courses if course.course_id == course_id]
        course = course_list[0] if course_list else None
        if course:
            return [student.name for student in course.enrolled_students]
    
    def retrieve_courses_for_student(self, student_id, str):
        student_list = [student for student in self.students if student.id_number == student_id]
        student = student_list[0] if student_list else None

        if student:
            return [enrollment.course.course_name for enrollment in self.enrollments if enrollment.student.id_number == student_id]