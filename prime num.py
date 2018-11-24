num=int(raw_input("the given  number "))
if num > 1:
	for i in range(2,num):	
		if (num % i) == 0:
			print("is not a prime number",num)
else:
	print("is a prime number",num)
 
