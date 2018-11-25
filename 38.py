s,n = map(int,raw_input().split())
s = s ^ n
n= s ^ n
s = s ^ n
print(" {0} {1}".format(s, n)),
