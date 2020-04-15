my_list=[5,4,3]

print(list(map(lambda item:  item * item , my_list)))


a = [(0, 2), (5, 2), (9, 9), (10, -1)]

print(a.sort(key=lambda x: len(x)))
print(a)