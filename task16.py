import os, binascii

def generate_password():
	return binascii.b2a_hex(os.urandom(20))

for i in range(5):
	print(generate_password())
