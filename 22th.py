# your code goes here
n,k=map(int,raw_input().split())
n=int(n)
k=int(k)
         
if n > k: 
    small = k
else: 
    small = n 
for i in range(1, small+1): 
    if((n % i == 0) and (k % i == 0)): 
        gcd = i 
print(gcd) 
