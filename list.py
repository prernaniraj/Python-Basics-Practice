l = [1,2,3,4,5]
l.insert(7,7)
print(l)
l.clear()
print(l)

#list comprehension
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate=list(set([item for item in some_list if some_list.count(item) > 1 ]))
print(duplicate)
print(some_list.reverse())
print(some_list)