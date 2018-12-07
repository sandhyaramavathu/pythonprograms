s,l = map(int,raw_input().split())
def gcd(b,n):
    z=abs(b-n)
    if (b-n)==0:
        return n
    else:
        return gcd(z,min(b,n))
print gcd(s,l)
