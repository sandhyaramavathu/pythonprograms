aptitude,bang,channel = [int(x) for x in raw_input().split()]
sum=0
for i in range(channel):
 sum+=aptitude+(i*bang)
print(sum)
