def common_elements_of_two_lists(a, b):
	result = []
	for elem in a:
		if elem in b and elem not in result:
			result.append(elem)
	return result

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("Intersection of two lists two ways:")
print(common_elements_of_two_lists(a, b))
print(set(a) & set(b))
