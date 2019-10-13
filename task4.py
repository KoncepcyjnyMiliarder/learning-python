def divisors(num):
	result = []
	for i in range(1, num+1):
		if num % i == 0:
			result.append(i)
	return result

def divisors_by_list_comprehension(num):
	return [x for x in range(1, num + 1) if num % x == 0]

def divisors_by_filter(num):
	return list(filter(lambda x : num % x == 0, range(1, num+1)))

num = 720
print("Divisors of", num, " with 3 different methods:")
print(divisors(num))
print(divisors_by_list_comprehension(num))
print(divisors_by_filter(num))
