import random

def get_sample():
	return set(random.sample(range(100), 25))

print("Samples:")
a = get_sample()
b = get_sample()
print(a)
print(b)
print("Intersection:", sorted(a & b))
print("Sum:", sorted(a | b))
print("Xor:", sorted(a ^ b))
