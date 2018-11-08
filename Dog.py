class Dog:
	def __init__(self, name):
		self.name = name
		print(self.name, " was Born")

	def speak(self):
		print("YELP!", self.name)

	def wag(self):
		print("Dog's wag tail")

	def __del__(self):
		print("destroy!!")


puddle = Dog("bori")
sheperd = Dog("ssal")

puddle.speak()
sheperd.speak()


class Puppy(Dog):
	def __init__(self):
		self.name = "Puppy"
		print("Puppy was Born")
def wag(self):
		print("Puppy's wag tail")

puppy = Puppy('PP')
puppy.speak()
print("Name is", puppy.name)
print("isDog", isinstance(puppy, Dog))
puppy.test()
marry = Dog()
