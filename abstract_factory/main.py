from abstract_factory.client import Client

if __name__ == '__main__':
    person1 = Client()
    person1.request_chair()
    person2 = Client()
    person2.request_chair()

    print(person1.chair)
    print()
    print()
    print(person2.chair)
