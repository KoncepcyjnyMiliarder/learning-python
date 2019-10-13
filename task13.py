def fibo_iter(index):
	a, b = 1, 1
	while index > 0:
		index -= 1
		a, b = b, a + b
	return a

def fibo_rec(index):
	if index < 2:
		return 1
	return fibo_rec(index - 1) + fibo_rec(index - 2)

fibos = list(map(lambda x : [fibo_iter(x), fibo_rec(x)], range(1, 30)))
list(map(print,fibos))
