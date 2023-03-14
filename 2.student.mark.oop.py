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
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}, DOB: {self.__dob}"
    
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
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}"

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
        print(course)

def list_students(students):
    print("List of students:")
    for student in students:
        print(student)

def show_course_marks(course):
    for mark in course.get_marks():
        print(f"{mark}")
    print(f"Average: {course.get_average()}")

def menu():
    print("1. Input students info")
    print("2. Input courses info")
    print("3. Input marks")
    print("4. List courses")
    print("5. List students")
    print("6. Show course marks")
    print("7. Show student info")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        input_students_info()
    elif choice ==2:
        input_courses_info()
    elif choice ==3:
        input_mark(courses, students)
    elif choice ==4:
        list_courses(courses)
    elif choice ==5:
        list_students(students)
    elif choice ==6:
        choose = input("Enter your course_id: ")
        for course in courses:
            if course.get_id() == choose:
                show_course_marks(course)
    elif choice ==7:
        choose2 = input("Enter your student_id: ")
        for student in students:
            if student.get_id() == choose2:
                print(student)
    elif choice ==8:
        exit()
while True:
    menu()

    
        
        




    