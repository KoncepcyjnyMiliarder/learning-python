import random

while True:
	line = input("Enter number or \"quit\" to leave the guessing game: ")
	if line == "quit":
		break;
	rand = random.randint(1, 9)
	num = int(line)
	while num != rand:
		if num > rand:
			print("Too high!")
		else:
			print("Too low!")
		num = int(input())
	print("That's right! The number was", rand)
