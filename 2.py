nature = int(raw_input())
fact = 1
if(fact == 0):
    print(1)
else:
    for i in range(1,nature+1):
        fact = fact*i
    print fact  
