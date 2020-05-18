dict ={ 
    'a' : 1,
    'b' : 2
}

dict1 = dict

dict['a'] = 3
dict1.pop('a')
print(dict1)