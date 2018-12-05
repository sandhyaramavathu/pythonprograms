# your code goes here
def isIsogram(n):
	charMap={}
	for h in n:
		if h in charMap:
			return False
		else:
			charMap[c]=1
	return True
n=raw_input().rstrip()
print("Yes" if isIsogram(n) else "No")
