class Pet(object):
    name = 'Pet'
    specie = 'Undefined'
    age = 0

    def __init__(self, name='Pet', age=0):
        self.name = name
        self.specie = 'Undefined'
        self.age = age


# Inherited all the attributes from the Pet class
class Dog(Pet):
    def __init__(self, name, age):
        # super().__init__()
        pass


# Inherited all the attributes from the Pet class
class Cat(Pet):
    def __init__(self, name, age):
        # Called Pet's __init__ with known name and age
        super().__init__(name, age)


# Inherited all the attributes from the Pet class
class Fish(Pet):
    def __init__(self, name, age):
        # Called Pet's __init__ with known name and age
        super().__init__(name, age)

        # Also overwriting Pet class's self.specie attribute
        self.specie = 'Fish'


class Rock(Pet):
    def __init__(self):
        # Inherited all the attributes from the Pet class
        pass