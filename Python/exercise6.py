def is_prime(a):
	for i in range(2,a):
		if(a%i)==0:
			return True
		else:
			return False
x=is_prime(11)
print(x)