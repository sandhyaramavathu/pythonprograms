
str = raw_input().rstrip()
even = odd = ''
for i, s in enumerate(str):
	if i & 1 == 0:
		even str += s
	else:
		oddstr += s

	print(evenstr + " " + oddstr)
