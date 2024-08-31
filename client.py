from sms import Person, Student, Instructor, Course, Enrollment, StudentManagementSystem

student_data = [
    {
        "name": "Adeyinka",
        "id_number": "ST01",
        "major": "Engineering"
    },
    {
        "name": "Bola",
        "id_number": "ST02",
        "major": "Literature"
    },
    {
        "name": "Mariam",
        "id_number": "ST03",
        "major": "Medicine"
    }
]

instructor_data = [
    {
        "name": "John",
        "id_number": "IN01",
        "department": "Art"
    },
    {
        "name": "Fatima",
        "id_number": "IN02",
        "department": "Science"
    },
    {
        "name": "Cynthia",
        "id_number": "IN03",
        "department": "Technology"
    }
]

course_data = [
    {
        "course_name": 'Introduction to Engineering',
        "course_id": "ENG101"
    },
    {
        "course_name": 'Introduction to Medicine',
        "course_id": "MED101"
    },
    {
        "course_name": 'Introduction to Literature',
        "course_id": "LIT101"
    }

]

my_sms = StudentManagementSystem()

for student in student_data:
    new_student = Student(**student)
    my_sms.add_student(new_student)

list_of_students = my_sms.get_students()
# print(list_of_students)

my_sms.remove_student("ST02")
# print(my_sms.get_students())

my_sms.update_students(id="ST03", updated_name="Maryam")
# print(my_sms.get_students())

for instructor in instructor_data:
    new_instructor = Instructor(**instructor)
    my_sms.add_instructor(new_instructor)

# print(my_sms.get_instructors())

my_sms.remove_instructor("IN01")
# print(my_sms.get_instructors())

my_sms.update_instructors(id="IN02", updated_department="Sociology")
# print(my_sms.get_instructors())

for course in course_data:
    new_course = Course(**course)
    my_sms.add_course(new_course)

# print(my_sms.get_courses())

my_sms.remove_course("LIT101")
# print(my_sms.get_courses())

# my_sms.update_course(id="MED101", updated_course_name="Medicine for beginners")
# print(my_sms.get_courses())

my_sms.enroll_student_in_course(student_id="ST01", course_id="ENG101")
my_sms.enroll_student_in_course(student_id="ST03", course_id="MED101")
my_sms.enroll_student_in_course(student_id="ST01", course_id="MED101")
# print(my_sms.get_enrollment())

my_sms.assign_student_grade_for_course(student_id="ST01", course_id="ENG101", grade=85)

students_in_course = my_sms.retrieve_student_in_course("ENG101")
for student in students_in_course:
    print(student)

course_for_student = my_sms.retrieve_courses_for_student(student_id="ST01")
for course in course_for_student:
    print(course)
