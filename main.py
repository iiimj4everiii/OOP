class Pet(object):
    def __init__(self, name='Pet', age=0):
        self.name = name
        self.specie = 'Undefined'
        self.age = age


class Dog(Pet):
    def __init__(self, name, age):
        # Called Pet's __init__
        super().__init__()


class Cat(Pet):
    def __init__(self, name, age):
        # Called Pet's __init__ with known name and age
        super().__init__(name, age)


class Fish(Pet):
    def __init__(self, name, age):
        # Called Pet's __init__ with known name and age
        super().__init__(name, age)

        # Also overwriting Base class's self.specie attribute
        self.specie = 'Fish'


class Rock(Pet):
    def __init__(self):
        # Did not inherit anything
        print("Since Rock's __init__ did not call Pet class's __init__, nothing has been inherited. "
              "Calling print('Name =', rock.name, 'Specie =', rock.specie, 'Age =', rock.age)\nwill result in "
              "AttributeError because rock did not inherit these attributes {name, specie, or age}.")


dog = Dog('Snoopy', 3)
print('Name =', dog.name, '\nSpecie =', dog.specie, '\nAge =', dog.age)


print()
cat = Cat('Garfield', 4)
print('Name =', cat.name, '\nSpecie =', cat.specie, '\nAge =', cat.age)

print()
fish = Fish('Nemo', 5)
print('Name =', fish.name, '\nSpecie =', fish.specie, '\nAge =', fish.age)

print()
rock = Rock()
# print('Name =', rock.name, '\nSpecie =', rock.specie, '\nAge =', rock.age)


import class_with_attributes as new_class

print()
print()
dog2 = new_class.Dog('Snoopy', 3)
print('Name =', dog2.name, '\nSpecie =', dog2.specie, '\nAge =', dog2.age)


print()
cat2 = new_class.Cat('Garfield', 4)
print('Name =', cat2.name, '\nSpecie =', cat2.specie, '\nAge =', cat2.age)

print()
fish2 = new_class.Fish('Nemo', 5)
print('Name =', fish2.name, '\nSpecie =', fish2.specie, '\nAge =', fish2.age)

print()
rock2 = new_class.Rock()
print('Name =', rock2.name, '\nSpecie =', rock2.specie, '\nAge =', rock2.age)
