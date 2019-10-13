def is_palindrome(str):
	return str == str[::-1]

a = ['ala', '123434', '12345654321', 'kajak', 'alamakota']
print("Palindromes: ", list(filter(lambda str : is_palindrome(str), a)))
