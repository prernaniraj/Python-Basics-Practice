list1 = [1,3,5,7,2]
list2 = [2,3,4,5,6,7,8,9,10]

ln_list1 = len(list1)
ln_list2 = len(list2)
if ln_list1 > ln_list2:
    bigger_list, smaller_list = list1,list2  
else:
    bigger_list, smaller_list = list2,list1
common_list = []
for num1 in smaller_list:
    if num1 in bigger_list and num1 not in common_list:
        common_list.append(num1)

print(common_list)