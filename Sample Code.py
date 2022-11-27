thistuple = ("Cheska", "Stephanie", "Christine", "Raine")
print(thistuple)


thisdict = {
  "brand": "Victoria's Secret",
  "scent": "Bare Vanilla",
  "year": 2018
}
print(thisdict)


thisdict = {
  "brand": "Victoria's Secret",
  "scent": "Bare Vanilla",
  "year": 2018
}
print(thisdict["scent"])


def my_function(fname):
  print(fname + " Manalo")

my_function("Edgardo")
my_function("Cristy Vee")
my_function("Cheska")
my_function("Christine")


def my_function(*kids):
  print("The older child is " + kids[0])

my_function("Cheska", "Christine")


def my_function(perfume):
  for x in perfume:
    print(x)

perfume = ["dahlia", "bare vanilla", "lacoste"]

my_function(perfume)


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(15))
print(mytripler(15))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Cheska", 20)

print(p1.name)
print(p1.age)






