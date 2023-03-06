#input functions
def inputNumberStudents():
    return int(input("Enter number of students: "))

def studentInfo():
    students = []
    studentname = input("Enter student name: ")
    studentid = input("Enter student id: ")
    studentdob = input("Enter student dob: ")
    students.append(studentname)
    students.append(studentid)
    students.append(studentdob)
    return students

def inputNumberCourses():
    return int(input("Enter number of courses: "))

def courseInfo():
    courses = []
    coursename = input("Enter course name: ")
    courseid = input("Enter course id: ")
    courses.append(coursename)
    courses.append(courseid)
    return courses

def inputMarks(courses, students):
    marks = []
    print(f"Enter mark for course: {courses[0]}")
    for student in students:
        mark = input(f"-Student {student[0]}: ")
        marks.append(mark)
    return marks

def ListStudents(students):
    print("List of students:")
    for student in students:
        print(f"-{student[0]}")

def ListCourses(courses):
    print("List of courses:")
    for course in courses:
        print(f"-{course[0]}")

def showCourseMarks(marks, students, courses):
    print(f"List of marks for course: {courses[0]}")
    for i in range(len(marks)):
        print(f"-{students[i][0]}: {marks[i]}")

#List functions
students = []
courses = []
marks = []

number_students = inputNumberStudents()
for i in range(number_students):
    students += [studentInfo()]

number_courses = inputNumberCourses()
for i in range(number_courses):
    courses += [courseInfo()]

for course in courses:
    marks += [inputMarks(course, students)]

ListStudents(students)
ListCourses(courses)
showCourseMarks(marks, students, courses)


