_,AA=map(int,raw_input().split(" "))
DATA=map(int,raw_input().split(" "))
l=len(DATA)
for __ in range(AA):
   DATA = [DATA[l-1]] + DATA[0:l-1]
print " ".join(map(str,DATA))
