import random

class Person :
  def __init__ (self,name,twitter,target):
    self.name = name
    self.twitter = twitter
    self.target = self.name + " (" + self.twitter + ")"

a = Person("Jacob", "@countj0ecool", None)
b = Person("Zeus", "@kingofdaheavens", None)
c = Person("Kasra", "@kasrakaley", None



print(a.name + "'s target is " + a.target)
print(b.name + "'s target is " + b.target)
print(c.name + "'s target is " + c.target)

def assassin(name, twitter, target):
  print(name + "(" + twitter + ")")

assassin("Jacob", "@countj0ecool", "Kasra(@kasrakaley)")
assassin("Zeus", "@kingofdaheavens","Jacob(@countj0ecool)")
assassin("Kasra", "@kasrakaley", "Zeus(@kingofdaheavens)")
