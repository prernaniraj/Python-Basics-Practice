class Abc:
    classVariable = "AAA"
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def prints(self):
        print(f'Hi {self.a} and {self.b}')
        Abc.classVariable = "CCC"

    def printClassVariable(self):
        print(self.classVariable)

Abc1 = Abc("p","n")
Abc1.prints()
Abc1.printClassVariable()
print(Abc1.__dict__)
a = {'p':1,'q':2, 'r':3}   
print(len(a))
print(Abc1.classVariable)
Abc.classVariable = "asdfsadf"

print(Abc1.classVariable)
print(dir(Abc1))
print(Abc1.__dir__)
print(Abc1.__dict__)
print(str(print))
print(len([1,2,3,4,5,6]))