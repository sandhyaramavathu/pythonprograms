def play_31():
	s=(raw_input())
	N1,N2=0,0
	for i in s:
		if i=='(':
			N1+=1
		if i==')':
			N2+=1
	if N1==N2:
		print('yes')
	else :
		print('no')
play_31()
		
