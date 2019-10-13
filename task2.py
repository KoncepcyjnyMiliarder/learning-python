num = int(input("Enter number: "))
if num % 2 == 0:
	print("Your number is even ", end ='')
	if num % 4 == 0:
		print("and divisible by 4!")
	else:
		print("but not divisible by 4")
else:
	print("The number is odd")

div = int(input("Enter another number: "))
if num % div == 0:
	print("The first number is divisble by the second")
