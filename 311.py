def play_31():
	S = (raw_input())
	B1,B2 = 0,0
	for i in S:
		if i == '(':
			B1+= 1
		if i == ')':
			B2+= 1
	if B1 == B2:
		print('RIGHT')
	else :
		print('WRONG')
play_31()
		
