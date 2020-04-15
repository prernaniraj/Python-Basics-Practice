class Class1:
    Class1Variable = 1
    def __init__(self,variable1):
        self.variable1 = variable1


instance = Class1("c")
print(instance.Class1Variable)
print(Class1.Class1Variable)
instance.Class1Variable = 'changed'
print(Class1.Class1Variable)
print(instance.Class1Variable)
Class1.Class1Variable ='2'
del instance.Class1Variable
print(instance.Class1Variable)
print(Class1.Class1Variable)
