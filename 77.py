n = int(raw_input())
count = 0
if n>0:
    for i in range(1,n+1):
        if n%i == 0:
            print i
