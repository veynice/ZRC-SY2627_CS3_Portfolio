class Animal:
	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def eat(self):
		print(f"{self.get_name()} eats.")

	def make_sound(self):
		print(f"{self.get_name()} makes a sound.")


class Lion(Animal):
	def eat(self):
		print(f"{self.get_name()} eats fresh meat.")

	def make_sound(self):
		print(f"{self.get_name()} roars loudly!")


class Elephant(Animal):
	def eat(self):
		print(f"{self.get_name()} eats grass and fruits.")

	def make_sound(self):
		print(f"{self.get_name()} trumpets!")


class Monkey(Animal):
	def eat(self):
		print(f"{self.get_name()} eats bananas.")

	def make_sound(self):
		print(f"{self.get_name()} chatters!")


animals = [Lion("Simba"), Elephant("Dumbo"), Monkey("George")]

for animal in animals:
	animal.make_sound()
	animal.eat()
	print("-" * 5)