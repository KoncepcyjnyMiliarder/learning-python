def remove_duplicates(a):
	return list(set(a))

a = [x**3 % 101 for x in range(200)]
print("Size of original list:", len(a))
print("After removing duplicates:", len(remove_duplicates(a)))
