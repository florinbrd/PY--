# 03.OOP


class PlayerChar:
    online_player = True  # static attribute

    def __init__(self, name):  # constructor with dynamic attributes
        self.name = name

    def run(self):  # function of the object
        print('run')


class PlayerTest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.online = False

    def change(self):
        self.online = True

    @classmethod
    def adding(cls, num1, num2):  # they don't need to be applied on instanstied
        return num1 + num2  # it also works PlayerTest.adding(1,2)

    @classmethod
    def newObject(cls, nu1, nu2):
        return cls('Florin', nu1 + nu2) # creates a new instance of the class

    @staticmethod
    def addnewthings(num1, num2):   # no access to the class, we use static when we don't care about attributes
        return num1 + num2


player1 = PlayerChar('Florin')  # creates the object
print(player1)  # prints the location of the object
player1.run()   # calls the function run of the object
print(player1.name)  # prints the attributes of the object

player3 = PlayerTest('Florin', 22)
print(player3.age)
help(player3)    # prints out the whole blueprint of the object
print(player3.online)
player3.change()
print(player3.online)
print(player3.adding(1,2))

player4 = PlayerTest.newObject(20,10)
print(player4.age)
print(player4.addnewthings(20,20))

# Encapsulation - > we keep the data in an object/ data vs functions

# abstraction - hiding information, giving info only on what is needed

# private vs public attributes
# we need to get around it as there no standard private
# where is __ it means it is a private variable self._age = age
# there is no true private variables

# Inheritance: new objects to take properties of existent objects

# users that can be wizards, elfs, archers etc.

class User():
    def sign_in(self):
        print('loggedin')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class archer(User):  # user is the parent class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows! arrows left : {self.num_arrows}')

    def arrow(self):
        print(f'attacking with arrows! arrows left : {self.num_arrows}')

    def runfast(self):
        print('he is running really fast ')

wizard1 = Wizard('Merlin', 50)
archer1 = archer('Robin', 100)

print(wizard1.attack())
print(wizard1.sign_in())

print(isinstance(wizard1, Wizard))  # method built in to check if an object is instance of a class
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# polymorphism
# allows us to redefine methods

def attack(char):
    char.attack()

attack(wizard1)
attack(archer1)

for item in [wizard1, archer1]:
    item.attack()

class Animal():
    def __init__(self, code):
        self.code = code

    def signin(self):
        print('The animal is signed in')

class Dog(Animal):
    def __init__(self, name, code):
        super().__init__(code)
       # Animal.__init__(self, code)
        self.name = name

    def attack(self):
        print(f'Dog {self.name} is attacking, run away')


dog1 = Dog('Robbie', 101010)
print(dog1.code)
dog1.attack()
dog1.signin()

# Introspection
# determine the object and what  is has access to

print(dir(dog1)) # what are the methods and functions the dog1 can access

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))

# multiple inheritance

class Hybrid(Wizard, archer):  # it has the power of wizards, archers and also run
    def __init__(self, name, power, arrows):
        archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hybrid1 = Hybrid('bob', 50, 1000)
print(hybrid1.attack())
print(hybrid1.arrow())
print(hybrid1.sign_in())


# MRO - method resolution order
# it is a rule to determine how to run it

class AA:
    num = 10

class BB(AA):
    pass


class CC(AA):
    num = 1

class DD(BB, CC):  # first it will go into B and after into C , later to A and after to obj class 
    pass

print(DD.num)

print(DD.mro())   # it reveals the order of i t






