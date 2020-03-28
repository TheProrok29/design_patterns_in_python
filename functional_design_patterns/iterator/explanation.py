a_list = [1, 2, 3]
my_iter = iter(a_list)
print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
