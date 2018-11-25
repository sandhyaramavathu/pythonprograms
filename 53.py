n = int(raw_input())
s = []
while(n > 0):
    dig = n % 10
    s.append(dig)
    n = n//10
print sum(s)
