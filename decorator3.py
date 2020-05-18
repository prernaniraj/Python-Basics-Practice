import functools

def decor(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        c = 'number is : '
        c = c + fun(*args,**kwargs)
        return c
    return wrapper
    
    
@decor 
def one(a):
    if a == 'one':
        return '1'
    elif a == 'two':
        return '2'


c = one('one')

print(c)
print(one.__name__)
help(one)