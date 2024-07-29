def add_course(courses, course_name):
    if course_name not in courses:
        courses[course_name] = {}
        print(f"Course '{course_name}' added.")
    else:
        print(f"Course '{course_name}' already exists.")

def register_student(courses, course_name, student_name):
    if course_name in courses:
        courses[course_name][student_name] = True # True indicates enrollment.
        print(f"Student '{student_name}' registered for '{course_name}'.")
    else:
        print(f"Course '{course_name}' not found.")

def remove_student(courses, course_name, student_name):
    if course_name in courses and student_name in courses[course_name]:
        del courses[course_name][student_name]
        print(f"Student '{student_name}' removed from '{course_name}'.")
    else:
        print(f"Student or course not found.")


def display_enrollments(courses):
    for course, students in courses.items():
        print(f"Course: {course}")
        for student in students:
            print(f"   Student: {student}")

online_courses = {}


add_course(online_courses, "Python Programming")
add_course(online_courses, "Data Science")
register_student(online_courses, "Python Programming", "Alice")
register_student(online_courses, "Data Science", "Bob")
remove_student(online_courses, "Data Science", "Alice")
display_enrollments(online_courses)