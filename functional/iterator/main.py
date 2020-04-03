from functional.iterator.iterator import MyIter

my_iter = MyIter(10000)

# for element in my_iter:
#     print(element, end=' ')

results = []
while True:
    for _ in range(100):
        results.append(next(my_iter))
    print(results)
    option = input('If you want exit press: y :')
    if option == 'y':
        break
print(results)
