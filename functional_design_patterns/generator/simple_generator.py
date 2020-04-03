def generator():
    yield 1
    # print('a')
    yield 2
    # print('b')
    yield 3
    # print('c')


my_generator = generator()

for element in my_generator:
    print(element, end=' ')

for element in my_generator:
    print(element, end=' ')
