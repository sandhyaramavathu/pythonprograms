aA=int(input())
sum1=0
while(aA>0):
    num=int(aA%10)
    sum1=(num*num)+sum1
    aA=int(aA/10)
print(sum1)
