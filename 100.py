number = int(raw_input())
def calcProduct(numeric):
	if(len(str(numeric)) == 1):
		return numeric 
	else:
		return (numeric%10*calcProduct(numeric/10))
print(calcProduct(2143))
