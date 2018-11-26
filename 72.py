n = raw_input()
s = set('aeiou')
if not s.isdisjoint(n):
    print ("yes")
else:
    print ("no")
