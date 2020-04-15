import inspect
c = False
print ("hi" if c else "off")
for i,j in enumerate(range(4,10,2)):
    print(i,j)

def highest_even(li):
    highest_even_no=li[0]
    for i in li:
        if i > highest_even_no and i%2 ==0:
            highest_even_no = i

    return highest_even_no



print(highest_even([10,1,2,3,4,8,11,44]))

a=2
b=3
print(b^a)