class Fruit:
  def __init__(self, fname):
    self.fruitname = fname

  def printfname(self):
    print(self.fruitname)

#Use the Person class to create an object, and then execute the printname method:

x = Fruit ("Apple")
x.printfname()