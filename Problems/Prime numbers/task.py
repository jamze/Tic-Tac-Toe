list = []
prime_numbers = [2]
for i in range(3, 1000):
    for j in range(2, i):
        list.append(i%j == 0)
    if not any(list):
        prime_numbers.append(i)
    list = []

#print(len(prime_numbers))
#print(*primes, sep=", ")
