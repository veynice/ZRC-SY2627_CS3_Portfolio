class Mother:
    def __init__(self):
        self.mothername = ""

    def get_mothername(self):
        return self.mothername

    def set_mothername(self, name):
        self.mothername = name

    def mother(self):
        print(self.mothername)

class Father:
    def __init__(self):
        self.fathername = ""

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def __init__(self):
        super().__init__()
        Father.__init__(self)
        self.sonname = ""

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def parents(self):
        print("Son    :", self.get_sonname())
        print("Father :", self.get_fathername())
        print("Mother :", self.get_mothername())

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()



print("\n Modify Values")
s1 = Son()
s1.fathername = "RAMA"
s1.mothername = "SITADIVA"
s1.set_sonname("KUSH")
s1.parents()

print("\n Second Object")
s2 = Son()
s2.set_fathername("Thomas")
s2.set_mothername("Martha")
s2.set_sonname("Bruce")
s2.parents()