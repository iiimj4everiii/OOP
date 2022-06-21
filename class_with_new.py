class Pet(object):
    def __init__(self, name='Pet', age=0):
        print("In __init__")
        self.name = name
        self.specie = 'Undefined'
        self.age = age

    def __new__(cls, name='Pet', age=0):
        print("In __new__")
        return super().__new__(cls)

print()
dog = Pet('Snoppy', 5)
print(dog.name)
print(dog.specie)
print(dog.age)

print()
cat = Pet()
print(cat.name)
print(cat.specie)
print(cat.age)
