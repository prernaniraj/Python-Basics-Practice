#Given the below class:
class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def get_age(cls,age):
        print(age)
        cat4=cls('Hi',age)
        print(cat4)


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('a',1)
cat2 = Cat('b',2)
cat3 = Cat('c',3)
# 2 Create a function that finds the oldest cat
Cat.get_age(4)
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'Oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old')