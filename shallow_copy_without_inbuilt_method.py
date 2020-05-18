info = {'other_info': {'a': 1, 'b': 2}, 'lst': ['c', 'd', 'e']}
new_info = {}

for key, value in info.items():
    if isinstance(value, dict):        
        temp_dict = {}
        for key2, value2 in value.items():
            temp_dict[key2] = value2
        new_info[key] = temp_dict
    elif isinstance(value, list):
        temp_lst = []
        for key2, value2 in enumerate(value):
            temp_lst.append(value2)
        new_info[key] = temp_lst

print(info)
print('-' * 50)
print(new_info)

print('-' * 50)
print(id(info))
print(id(new_info))
