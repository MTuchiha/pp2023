students = []
courses = []
class student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dob(self):
        return self.__dob
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_dob(self, dob):
        self.__dob = dob
    
class course:
    marks = []
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def add_mark(self, mark):
        self.marks.append(mark)
    def get_marks(self):
        return self.marks
    def get_average(self):
        total = 0
        for i in self.marks:
            total += i
        return total/len(self.marks)

def input_number_students():
    return int(input("Enter number of students: "))

def input_students_info():
    for i in range(input_number_students()):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        students.append(student(name, id, dob))

def input_number_ourses():
    return int(input("Enter number of courses: "))

def input_courses_info():
    for i in range(input_number_ourses()):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append(course(name, id))

def input_mark(courses, students):
    for course in courses:
        print(f"Enter mark for course: {course.get_name()}")
        for student in students:
            mark= int(input(f"-Student {student.get_name()}: "))
            course.add_mark(mark)

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"-{course.get_name()}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"-{student.get_name()}")

def show_course_marks(course):
    for mark in course.get_marks():
        print(f"-{mark}")


input_students_info()
input_courses_info()
input_mark(courses, students)
list_courses(courses)
list_students(students)
for course in courses:
    print(f"List of marks for {course.get_name()}:")
    show_course_marks(course)
    print(f"Average mark for {course.get_name()}: {course.get_average()}")




    