import curses
import math
import numpy as np

class student:
    def __init__(self, name, dob, id):
        self.__name = name
        self.__dob = dob
        self.__id = id
        self.marks_array = np.array([])
        self.credit_array = np.array([])
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_id(self):
        return self.__id
    def set_mark(self, mark):
        self.marks_array = np.append(self.marks_array, mark)
    def set_credit(self, credit):
        self.credit_array = np.append(self.credit_array, credit)
    def get_mark(self):
        return self.__mark
    def get_average(self):
        return np.average(self.marks_array, weights=self.credit_array)
    def get_gpa(self):
        return round(self.get_average(), 1)
class course:
    def __init__(self, name, id, credits):
        self.__name = name
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_credits(self):
        return self.__credits

class manager:
    def __init__(self):
        self.__student_list = []
        self.__course_list = []
    
    def add_students(self, stdcrs):
        stdcrs.clear()
        stdcrs.addstr("Enter number of students: ")
        num_students = int(stdcrs.getstr().decode())
        for i in range(num_students):
            stdcrs.addstr(f"\nEnter details for student {i + 1}\n")
            stdcrs.addstr("Name: ")
            name = stdcrs.getstr().decode()
            stdcrs.addstr("Date of birth: ")
            dob = stdcrs.getstr().decode()
            stdcrs.addstr("ID: ")
            id = int(stdcrs.getstr().decode())
            self.__student_list.append(student(name, dob, id))
           
    
    def add_courses(self, stdcrs):
        stdcrs.clear()
        stdcrs.addstr("Enter number of courses: ")
        num_courses = int(stdcrs.getstr().decode())
        for i in range(num_courses):
            stdcrs.addstr(f"\nEnter details for course {i + 1}\n")
            stdcrs.addstr("Name: ")
            name = stdcrs.getstr().decode()
            stdcrs.addstr("ID: ")
            id = int(stdcrs.getstr().decode())
            stdcrs.addstr("Credits: ")
            credits = int(stdcrs.getstr().decode())
            self.__course_list.append(course(name, id, credits))
    def view_students(self, stdcrs):
        stdcrs.clear()
        stdcrs.addstr("Name\t\tDate of birth\t\tID\t\tGPA")
        for i in self.__student_list:
            stdcrs.addstr(f"{i.get_name()}\t\t{i.get_dob()}\t\t{i.get_id()}\t\t{i.get_gpa()}")
    def view_courses(self, stdcrs):
        stdcrs.clear()
        stdcrs.addstr("Name\t\tID\t\tCredits")
        for i in self.__course_list:
            stdcrs.addstr(f"{i.get_name()}\t\t{i.get_id()}\t\t{i.get_credits()}")
    def main(self, stdcrs):
        while True:
            stdcrs.clear()
            stdcrs.addstr("1. Add students\n")
            stdcrs.addstr("2. Add courses\n")
            stdcrs.addstr("3. View students\n")
            stdcrs.addstr("4. View courses\n")
            stdcrs.addstr("5. Exit\n")
            stdcrs.addstr("Enter your choice: ")
            choice = int(stdcrs.getstr().decode())
            if choice == 1:
                self.add_students(stdcrs)
            elif choice == 2:
                self.add_courses(stdcrs)
            elif choice == 3:
                self.view_students(stdcrs)
            elif choice == 4:
                self.view_courses(stdcrs)
            elif choice == 5:
                break
            stdcrs.getkey()
def main(stdcrs):
    manager().main(stdcrs)
curses.wrapper(main)



