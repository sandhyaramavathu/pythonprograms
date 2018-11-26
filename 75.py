ns = raw_input()
p = len(ns)
s = list(ns)
if p%2 == 0:
    m= p/2 - 1
    s[m] = '*'
    s[m+1] = '*'
else:
    m = p/2 - 1
    s[m+1] = '*'
print "".join(s)
