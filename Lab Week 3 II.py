# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 05:38:46 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    # Added 'self' parameter
    def __init__(self):  
        self.a = 10
        self.b = 20
        self.x = self.a + self.b  

my_instance = MyClass()
print(my_instance.x)


#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        # Store the result of a + b 
        self.x = a + b  
    
    def get_x(self):
        return self.x  

my_instance = MyClass()
print(my_instance.get_x())


#3
class MyClass():
    # Added 'self' as the first parameter
    def __init__(self, a, b):  
        self.x = a + b

my_instance = MyClass(10, 20)
print(my_instance.x)



#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.enrolled_courses = []

    def enroll(self, course_name, course_number, days, times):
        course = {
            "course_name": course_name,
            "course_number": course_number,
            "days": days,
            "times": times
        }
        # Simple validation to ensure no duplicate courses are added
        for existing_course in self.enrolled_courses:
            if existing_course["course_number"] == course_number:
                print(f"Already enrolled in {course_name}.")
                return
        self.enrolled_courses.append(course)

    def drop_course(self, course_number):
        for course in self.enrolled_courses:
            if course["course_number"] == course_number:
                self.enrolled_courses.remove(course)
                print(f"Dropped {course['course_name']}.")
                return
        print("Course not found.")

    def display_courses(self):
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            for course in self.enrolled_courses:
                print(f"{course['course_name']} ({course['course_number']}) - {course['days']} at {course['times']}")

# Test the functionality
student = Student("SHIHAN ZHAO", 2024)
student.enroll("Data and Programming for Public Policy I - Python Programming", "PPHA 30537", "TTH", "11:00am-12:20pm")
student.enroll("Applied Financial Management", "PPHA 42510", "MW", "10:30am-11:50am")
student.display_courses()

# Attempt to enroll in a duplicate course
student.enroll("Data and Programming for Public Policy I - Python Programming", "PPHA 30537", "TTH", "11:00am-12:20pm")

# Drop a course
student.drop_course("PPHA 42510")
student.display_courses()





