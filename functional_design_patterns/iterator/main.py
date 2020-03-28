from iterator import MyIter

my_iter = MyIter(100)

# for element in my_iter:
#     print(element, end=' ')

my_iter_as_list = list(my_iter)
print(my_iter_as_list)
