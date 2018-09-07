num = int(input("the given number is:"))
if num < 0:
	print"not valied"
elif num == 0:
	print"not valied"
else:
	for i in range(2,num):
		if(num % i) == 0:
			print"is a prime number"
