class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, name):
        self.grandfathername = name 

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        super().__init__(grandfathername)

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

print("\n Modifying Values")
s1.set_grandfathername('Hadassah')
s1.set_fathername('Bless')
s1.set_sonname('Jemyx')
s1.print_name()

print("\nCreating a Second Object")
s2 = Son('Allam', 'Dave', 'Constantine')
s2.print_name()