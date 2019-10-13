from functools import reduce

def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

print("Primes until 200:")
primes = list(filter(is_prime, range(1, 201)))
print(primes)
print("Sum of these primes is", reduce(lambda x, y: x + y, primes))
