from abc import ABC, abstractmethod

class VEHICLE(ABC):
    def __init__(self,name):
        self.name = name

    def printVehicleName(self):
        print(self.name)

    @abstractmethod
    def set_wheel_count(self,wheels):
        pass
    @abstractmethod
    def test(self):
        pass

class car(VEHICLE):
    def test(self):
        print("inside car test method")

class NXON(car):
    def __init__(self,name):
        super().__init__(name)
        self.name = name

    def set_wheel_count(self,wheels):
        self.wheels = wheels
        print(f"wheel count is {self.wheels}")


car_obj = NXON('Nexon xz+')
car_obj.printVehicleName()
car_obj.set_wheel_count(4)
car_obj.test()