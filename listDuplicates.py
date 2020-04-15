list1=['a','b','c','b','d','m','n','n']
s = set(list1)
d={i:list1.count(i)for i in s}

duplicates=[]
for k,v in d.items():
    if v > 1:
        duplicates.append(k)

print(duplicates)
duplicates1 = []
for item in list1:
    if list1.count(item) > 1 and item not in duplicates1:
        duplicates1.append(item)
print(duplicates1)