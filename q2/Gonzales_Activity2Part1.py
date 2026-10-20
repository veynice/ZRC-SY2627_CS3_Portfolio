class Parent:
    def __init__(self, name="Parent Class"):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def func1(self):
        print(f"{self.get_name()}")


class Child(Parent):
    def __init__(self, name="Child Class", child_age=15):
        super().__init__(name)
        self._child_age = child_age

    def get_child_age(self):
        return self._child_age

    def set_child_age(self, new_age):
        self._child_age = new_age

    def func2(self):
        print(f"{self.get_name()} (Age: {self.get_child_age()})")

obj1 = Child("First Child", 15)
obj1.func1()
obj1.func2()

print("\n Setters ")
obj1.set_name("Updated First Child Age")
obj1.set_child_age(18)
obj1.func2()

print("\n Creating a Second Object")
obj2 = Child("Second Child", 23)
obj2.func1()
obj2.func2()
