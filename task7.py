def filter_out_odd(l):
	return list(filter(lambda x : x % 2 == 0, l))

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Even numbers are: ", filter_out_odd(a))
print("Odd numbers are: ", [x for x in a if x % 2 == 1])
