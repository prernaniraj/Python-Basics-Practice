def devision(a):
    while True:
        try:
            b = int(input("Enter number"))
            if b == 2:
                print("raising")
                raise noTwo(2)
            c = a/b
        except Exception as err:
            print(err)
            continue
        except noTwo as err:
            print(err)
        else:
            print(f'Division {a}/{b} is {c}')
            break
        finally:
            print("finally")
 
class noTwo(BaseException):
    def __init__(self,value):
        self.value = "Devide by two"

    def __str__(self)
        return(repr(self.value))


devision(220)