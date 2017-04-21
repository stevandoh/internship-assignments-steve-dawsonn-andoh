
class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):

        self.name = name

class Cat(Animal):
    
    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name

        #Person has-a pert of some kind
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):

        super(Employee, self).__init__(name)

        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan  is-a cat lol
satan = Cat("Satan")

## mary is-a Person pet

mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a n employee
frank = Employee("Frank", 12000)

# frank has-a pet called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

##
harry = Halibut()

