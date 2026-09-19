class Student:

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id


class Course:

    def __init__(self, course_name: str):
        self.course_name = course_name
        self.students = [] 

    def add_student(self, student: Student):
        self.students.append(student)



if __name__ == "__main__":
    course = Course("Computer Science")
    student1 = Student("Venice", "SN01")
    student2 = Student("Nicole", "SN02")

   
    course.add_student(student1)
    course.add_student(student2)

    
    enrolled_names = [s.name for s in course.students]
    print(f"Course: {course.course_name}")
    print(f"Enrolled Students: {enrolled_names}")
