class Parent:
    def __init__(self, parentname = "Parent"):
        self.parentname = parentname

    def get_parentname(self):
        return self.parentname

    def set_parentname(self, name):
        self.parentname = name

    def func1(self):
        print(f"[{self.get_parentname()}] Executing func1 from Parent class.")

class Child1(Parent):
    def __init__(self, parentname = "Parent", child1name = "Child 1"):
        super().__init__(parentname)
        self.child1name = child1name

    def get_child1name(self):
        return self.child1name

    def set_child1name(self, name):
        self.child1name = name

    def func2(self):
        print(f"[{self.get_child1name()}] Executing func2 from Child1 class.")

class Child2(Parent):
    def __init__(self, parentname = "Parent", child2name = "Child 2", role = "Sub Class"):
        super().__init__(parentname)
        self.child2name = child2name

    def get_child2name(self):
        return self.child2name

    def set_child2name(self, name):
        self.child2name = name

    def func3(self):
        print(f"[{self.get_child2name()}] (Parent: {self.get_parentname()}) Executing func3.")

object1 = Child1("Uno", "First SubClass")
object2 = Child2("Dos", "Second SubClass")

object1.func1()
object1.func2()
print()
object2.func1()
object2.func3()

print("\n Modifying Values ")
object1.set_parentname("Uno has been modified.")
print("Updated Parent Name:", object1.get_parentname())
object1.func2()

object2.set_parentname("Dos has been modified.")
object2.set_child2name("second SubClass has been updated.")
object2.func3()

print("\n Third Object")
object3 = Child1("Tres", "Third SubClass")
object3.func1()
object3.func2()