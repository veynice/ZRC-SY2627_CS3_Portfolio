class School:
    def __init__(self, school_name= "Philippine Science High School"):
        self.school_name = school_name

    def get_school_name(self):
        return self.school_name

    def set_school_name(self, school_name):
        self.school_name = school_name

    def func1(self):
        print(f"[{self.get_school_name()}] Executing func1 from School class.")


class Student1(School):
    def __init__(self, school_name="Philippine Science High School", student1_name="Student 1"):
        super().__init__(school_name)
        self.student1_name = student1_name

    def get_student1_name(self):
        return self.student1_name

    def set_student1_name(self, name):
        self.student1_name = name

    def func2(self):
        print(f"[{self.get_student1_name()}] (School: {self.get_school_name()}) Executing func2 from Student1 class.")


class Student2(School):
    def __init__(self, school_name = "Philippine Science High School", student2_name = "Student 2"):
        super().__init__(school_name)
        self.student2_name = student2_name

    def get_student2_name(self):
        return self.student2_name

    def set_student2_name(self, name):
        self.student2_name = name

    def func3(self):
        print(f"[{self.get_student2_name()}] (School: {self.get_school_name()}) Executing func3 from Student2 class.")


class Student3(Student1, School):
    def __init__(self, school_name = "Philippine Science High School", student1_name = "Student 1", student3_name = "Student 3"):
        super().__init__(school_name, student1_name)
        self.student3_name = student3_name

    def get_student3_name(self):
        return self.student3_name

    def set_student3_name(self, name):
        self.student3_name = name

    def func4(self):
        print(f"[{self.get_student3_name()}] (Track: {self.get_student1_name()}, School: {self.get_school_name()}) Executing func4 from Student3 class.")


obj1 = Student3("Bio Core", "STEM", "Ali")
obj1.func1()
obj1.func2()
obj1.func4()


print("\n Modifying Values via Setters ")
obj1.set_school_name("Updated Core")
obj1.set_student1_name("Advanced STEM")
obj1.set_student3_name("Ali (Senior)")
obj1.func2()
obj1.func4()

print("\n Creating a Second Object ")
obj2 = Student2("Physics Core", "Milan")
obj2.func1()
obj2.func3()