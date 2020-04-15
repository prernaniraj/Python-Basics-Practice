def extra_power(fun):
    def power():
        print("********")
        fun()
        print("********")
    return power

@extra_power
def fun1():
    print('baseFunction')

    
fun1()


