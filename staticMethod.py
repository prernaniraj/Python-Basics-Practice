class Person:
    classvariable =2
    def __init__(self,nm,age,city):
        self.nm = nm
        self.age = age
        self.city = city

    def printAge(self):
        print(f'{self.nm}\'s age is {self.age}')
    
    @staticmethod
    def isAdult(age):
        
        print("Adult") if age > 18 else print('Not Adult')

    @classmethod
    def classmethod1(cls):
        cls.classvariable += 1
        cls.age=3
        print(cls.classvariable)


person1 = Person('Prerna', 30, 'Colonia')
person1.isAdult(person1.age)
person1.printAge()
person1.classvariable =4
person1.classmethod1()
print(person1.classvariable)
person2 = Person('Niraj',33,'Colonia')
person2.isAdult(person2.age)
del person1.classvariable
person2.isAdult(person2.age)
print(Person.age)