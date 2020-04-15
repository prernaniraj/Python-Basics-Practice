class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
super_list1.extend({2,3,4,6})
print(len(super_list1))
print(super_list1)
print(isinstance(super_list1,SuperList))