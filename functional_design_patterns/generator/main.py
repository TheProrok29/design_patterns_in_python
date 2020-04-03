from functional_design_patterns.generator.prime_generator import prime_generator

x = prime_generator()
while True:
    last_primes = []
    for _ in range(100):
        last_primes.append(next(x))
    print(last_primes)
    option = input('If exit press y: ')
    if option == 'y':
        break
