from functools import reduce

def filter_smaller_elements(elems, top_val):
	result = []
	for number in elems:
		if number < top_val:
			result.append(number)
	return result

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
smaller_than_six = filter_smaller_elements(a, 6)
print("Elements smaller than 6 are", smaller_than_six)
print("Elements smaller than 66 are", filter_smaller_elements(a, 66))
print("One liners!")
print("Filtering between 6 and 40", list(filter(lambda x : x > 6 and x < 40, a)))
print("Squared:", list(map(lambda x : x**2, a)))
print("Product:", reduce(lambda x, y : x * y, a))
print("Sum", reduce(lambda x, y : x + y, a))
